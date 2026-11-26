# RAG do zero
 
Um sistema de perguntas e respostas sobre as minhas próprias notas, feito em Python puro, sem LangChain, LlamaIndex ou banco vetorial. A ideia foi montar cada peça de um RAG (Retrieval-Augmented Generation) na mão para entender o que acontece por baixo dos frameworks.
 
Você escreve uma pergunta no terminal, o programa encontra as notas mais parecidas com ela e manda esses trechos para o modelo responder. A resposta vem baseada só no que está nas notas, com a fonte de cada informação.
 
## Como funciona
 
O fluxo tem duas partes.
 
**Preparação (roda uma vez ao abrir o programa)**
 
1. Lê todos os arquivos `.md` da pasta `notas/`.
2. Gera o embedding de cada nota, ou seja, transforma o texto num vetor de 1536 números que representa o significado dele.
**A cada pergunta**
 
3. Gera o embedding da pergunta, com o mesmo modelo.
4. Compara o vetor da pergunta com o vetor de cada nota usando similaridade de cosseno. Cada nota ganha um score.
5. Ordena pelo score e pega as 3 notas mais parecidas.
6. Monta um contexto com essas notas, cada uma identificada pelo nome do arquivo.
7. Manda o contexto e a pergunta para o modelo, com a instrução de responder só com base nas notas e dizer quando não encontrar a resposta.
Os passos 3 a 5 são o R (a busca), o 6 é o A (a pergunta "aumentada" com os trechos) e o 7 é o G (a geração da resposta).
 
## O que dá para aprender com este projeto
 
- **O que é um embedding**: como um texto vira uma lista de números e por que frases com o mesmo significado ficam próximas, mesmo sem palavras em comum.
- **Similaridade de cosseno implementada na mão**: produto escalar, norma (módulo) do vetor e o que o resultado entre -1 e 1 significa.
- **Por que, com os vetores da OpenAI, o cosseno e o produto escalar dão praticamente o mesmo resultado**: os vetores já vêm com comprimento próximo de 1.
- **Busca semântica x busca por palavra-chave**: a busca acha a nota certa pelo sentido da pergunta, não pelas palavras exatas.
- **Por que a pergunta e as notas precisam usar o mesmo modelo de embedding.**
- **Como montar o contexto e as instruções** para o modelo responder só com o que foi fornecido e não inventar (alucinar).
- **Organização do código em funções com uma responsabilidade cada**, o que facilita trocar uma peça sem mexer no resto.
No arquivo `etapa1.py` estão os experimentos que fiz antes do RAG: comparar frases entre si para ver na prática como o modelo enxerga semelhança.
 
## Estrutura
 
```
├── etapa1.py         # experimentos com frases: embeddings e cosseno
├── etapa2.py         # o RAG completo
├── notas/            # as notas em .md que servem de base de conhecimento
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
 
E quando a resposta não está nas notas:
 
```
> Me fale sobre a história do Brasil
Não encontrei informações sobre a história do Brasil nas notas fornecidas.
```
 
## Limitações conhecidas
 
- A busca sempre devolve 3 notas, mesmo quando nenhuma tem a ver com a pergunta. Quem segura é a instrução do modelo.
- Cada nota vira um vetor inteiro. Em notas longas, que falam de vários assuntos, um trecho relevante pode se perder.
- Os embeddings são gerados de novo toda vez que o programa abre.
- Cada pergunta é independente: o programa não lembra da conversa anterior.
## Próximos passos
 
- [ ] Cortar as notas em pedaços (chunking) antes de gerar os embeddings
- [ ] Limite mínimo de score para responder "não encontrei" sem chamar o modelo
- [ ] Salvar os vetores em arquivo para não recalcular a cada execução
- [ ] Versão em Laravel, com os vetores guardados num banco vetorial
## Tecnologias
 
- Python
- API da OpenAI: `text-embedding-3-small` para os embeddings e `gpt-5-mini` (Responses API) para as respostas
 