# RAG do zero
 
Um sistema de perguntas e respostas sobre as minhas próprias notas, feito em Python puro, sem LangChain, LlamaIndex ou banco vetorial. A ideia foi montar cada peça de um RAG (Retrieval-Augmented Generation) na mão para entender o que acontece por baixo dos frameworks.
 
Você escreve uma pergunta no terminal, o programa encontra os trechos das notas mais parecidos com ela e manda esses trechos para o modelo responder. A resposta vem baseada só no que está nas notas, com a fonte de cada informação.
 
## Como funciona
 
O fluxo tem duas partes.
 
**Preparação (roda uma vez ao abrir o programa)**
 
1. Lê todos os arquivos `.md` da pasta `notas/` (arquivos vazios são ignorados).
2. Corta cada nota em pedaços (chunks), um por parágrafo, usando a linha em branco (`

`) como separador. Cada pedaço guarda o nome da nota de onde veio e a sua posição nela.
3. Gera o embedding de cada pedaço, ou seja, transforma o texto num vetor de 1536 números que representa o significado dele. Todos os pedaços vão numa única chamada à API.

**A cada pergunta**
 
4. Gera o embedding da pergunta, com o mesmo modelo.
5. Compara o vetor da pergunta com o vetor de cada pedaço usando similaridade de cosseno. Cada pedaço ganha um score.
6. Ordena pelo score, pega os 3 pedaços mais parecidos e descarta os que ficaram abaixo do limite mínimo (`LIMITE_SCORE = 0.4`).
7. Se nenhum pedaço passou do limite, responde "Essa informação não está nos documentos" direto, sem chamar o modelo.
8. Se passou, monta um contexto com esses pedaços, cada um identificado pelo nome da nota.
9. Manda o contexto e a pergunta para o modelo, com a instrução de responder só com base nas notas, citar a fonte e dizer quando não encontrar a resposta.

Os passos 4 a 7 são o R (a busca), o 8 é o A (a pergunta "aumentada" com os trechos) e o 9 é o G (a geração da resposta).

### Por que cortar as notas em pedaços

Quando a nota inteira virava um único vetor, uma nota longa que fala de vários assuntos (como `notas/12_miscelanea.md`) ficava com um vetor que é uma "média" de tudo, e não se parecia muito com nenhuma pergunta específica. Com um vetor por parágrafo, a busca encontra exatamente o trecho que responde à pergunta, e o modelo recebe menos texto irrelevante.

O código tem duas formas de cortar:

- `dividir_por_paragrafo(texto)`: a que está em uso. Respeita a estrutura do texto, então nenhum pedaço corta uma frase no meio.
- `dividir_em_chunks(texto, tamanho, sobreposicao)`: a alternativa, por tamanho fixo em caracteres e com sobreposição entre um pedaço e o próximo, para uma informação que cai na fronteira não ficar dividida entre dois pedaços. Útil para textos sem parágrafos bem definidos.

### Limite mínimo de score

Antes, a busca sempre devolvia 3 notas, mesmo quando nenhuma tinha a ver com a pergunta, e quem segurava era a instrução do modelo. Agora os pedaços com score abaixo de `LIMITE_SCORE` são descartados, e se não sobrar nenhum o programa responde sem gastar uma chamada ao modelo. O valor fica no topo do `etapa2.py`, para ser ajustado: alto demais e perguntas válidas ficam sem resposta, baixo demais e trechos sem relação voltam a passar.
 
## O que dá para aprender com este projeto
 
- **O que é um embedding**: como um texto vira uma lista de números e por que frases com o mesmo significado ficam próximas, mesmo sem palavras em comum.
- **Similaridade de cosseno implementada na mão**: produto escalar, norma (módulo) do vetor e o que o resultado entre -1 e 1 significa.
- **Por que, com os vetores da OpenAI, o cosseno e o produto escalar dão praticamente o mesmo resultado**: os vetores já vêm com comprimento próximo de 1.
- **Busca semântica x busca por palavra-chave**: a busca acha o trecho certo pelo sentido da pergunta, não pelas palavras exatas.
- **Chunking**: por que dividir os documentos antes de gerar os embeddings, e a diferença entre cortar por parágrafo e por tamanho fixo com sobreposição.
- **Limite de score**: como usar o próprio score da busca para decidir que a resposta não está nas notas, antes de chamar o modelo.
- **Por que a pergunta e as notas precisam usar o mesmo modelo de embedding.**
- **Como montar o contexto e as instruções** para o modelo responder só com o que foi fornecido e não inventar (alucinar).
- **Organização do código em funções com uma responsabilidade cada**, o que facilita trocar uma peça sem mexer no resto (por exemplo, trocar a forma de cortar as notas).

No arquivo `etapa1.py` estão os experimentos que fiz antes do RAG: comparar frases entre si para ver na prática como o modelo enxerga semelhança.
 
## Estrutura
 
```
├── etapa1.py         # experimentos com frases: embeddings e cosseno
├── etapa2.py         # o RAG completo
├── notas/            # as notas em .md que servem de base de conhecimento
│   └── 12_miscelanea.md  # nota longa com vários assuntos, para testar o chunking
├── requirements.txt
└── .env              # sua chave da OpenAI (não vai para o repositório)
```
 
## Como rodar
 
```bash
git clone URL_DO_REPOSITORIO
cd rag-do-zero
 
python -m venv venv
source venv/bin/activate        # no Windows (Git Bash): source venv/Scripts/activate
 
pip install -r requirements.txt
```
 
Crie um arquivo `.env` na raiz com a sua chave:
 
```
OPENAI_API_KEY=sua-chave-aqui
```
 
Coloque os seus arquivos `.md` na pasta `notas/` e rode:
 
```bash
python etapa2.py
```
 
Digite uma pergunta depois do `>`. Para encerrar, digite `sair`.
 
## Exemplo
 
```
> Quero aprender sobre python
Segue um resumo do que as notas contêm sobre Python:
 
- O que é: linguagem de alto nível criada por Guido van Rossum e lançada em 1991. [01_python.md]
- Gerenciador de pacotes: pip instala bibliotecas do repositório PyPI. [01_python.md]
- Ambientes virtuais: criados com "python -m venv" para isolar dependências. [01_python.md]
...
```
 
E quando nenhum trecho passa do limite de score (o modelo nem é chamado):
 
```
> Me fale sobre a história do Brasil
Essa informação não está nos documentos
```

Se algum trecho passar do limite mas não tiver a resposta, quem diz que não encontrou é o próprio modelo, seguindo a instrução.
 
## Limitações conhecidas
 
- Os títulos em Markdown (`# Python`, `## Linux`) viram pedaços sozinhos, e os parágrafos perdem o título da seção a que pertencem. Um parágrafo que só faz sentido com o título pode não ser encontrado.
- Um parágrafo muito longo vira um pedaço só, e parágrafos curtos demais têm pouco significado para o embedding.
- O contexto identifica cada pedaço só pelo nome da nota, sem dizer qual parte é.
- O `LIMITE_SCORE` é um valor fixo. Pode precisar de ajuste com outras notas ou outro modelo de embedding.
- Os embeddings são gerados de novo toda vez que o programa abre.
- Todos os pedaços são enviados numa única chamada de embeddings, o que tem limite de tamanho se a pasta de notas crescer muito.
- Cada pergunta é independente: o programa não lembra da conversa anterior.
## Próximos passos
 
- [x] Cortar as notas em pedaços (chunking) antes de gerar os embeddings
- [x] Limite mínimo de score para responder "não encontrei" sem chamar o modelo
- [ ] Juntar o título da seção a cada parágrafo, para o pedaço não perder o contexto
- [ ] Salvar os vetores em arquivo para não recalcular a cada execução
- [ ] Versão em Laravel, com os vetores guardados num banco vetorial

## Tecnologias
 
- Python
- API da OpenAI: `text-embedding-3-small` para os embeddings e `gpt-5-mini` (Responses API) para as respostas
 