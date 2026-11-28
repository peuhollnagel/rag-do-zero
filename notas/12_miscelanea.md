# Miscelânea

Esta nota reúne assuntos variados, sem relação entre si, escritos em sequência. Alguns tópicos são longos e outros curtos, de propósito.

## Linux

Linux é um núcleo (kernel) de sistema operacional de código aberto anunciado por Linus Torvalds em 25 de agosto de 1991, quando ele ainda era estudante na Universidade de Helsinque, na Finlândia. Na mensagem original, publicada em um grupo de discussão da Usenet, Torvalds descreveu o projeto como "apenas um hobby, não será grande e profissional como o GNU".

Tecnicamente, "Linux" é só o kernel: a parte que gerencia memória, processos, dispositivos e o sistema de arquivos. Um sistema completo junta o kernel com ferramentas do projeto GNU, iniciado por Richard Stallman em 1983, e por isso alguns preferem o nome GNU/Linux. O kernel é distribuído sob a licença GPL versão 2.

Uma distribuição (ou "distro") é um pacote que combina o kernel, um gerenciador de pacotes, utilitários e, às vezes, um ambiente gráfico. O Debian foi criado por Ian Murdock em 1993. O Ubuntu, baseado no Debian e mantido pela empresa Canonical, teve sua primeira versão em outubro de 2004. Outras distros conhecidas são Fedora, Arch Linux, openSUSE e Linux Mint. O Android também usa o kernel Linux, o que faz dele o kernel mais instalado do mundo.

As permissões de arquivos no Linux são divididas em três grupos: dono, grupo e outros. Cada grupo pode ter permissão de leitura (r, valor 4), escrita (w, valor 2) e execução (x, valor 1). O comando "chmod 755 arquivo" dá permissão total ao dono (4+2+1 = 7) e leitura e execução aos demais (4+1 = 5), o que aparece como rwxr-xr-x. O usuário "root" é o administrador do sistema, e o comando sudo permite executar comandos com os privilégios dele.

Comandos básicos do terminal: ls lista arquivos, cd muda de diretório, pwd mostra o diretório atual, cp copia, mv move ou renomeia, rm remove, grep busca texto, ps lista processos e kill envia sinais para encerrá-los.

## Sistema Solar

O Sistema Solar tem oito planetas: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno. Os quatro primeiros são rochosos; Júpiter e Saturno são gigantes gasosos; Urano e Netuno são chamados de gigantes de gelo.

Plutão foi considerado o nono planeta desde sua descoberta, em 1930, por Clyde Tombaugh. Em 2006, a União Astronômica Internacional (UAI), reunida em Praga, definiu formalmente o que é um planeta e reclassificou Plutão como planeta anão, porque ele não "limpou" a vizinhança de sua órbita.

Júpiter é o maior planeta, com massa cerca de 2,5 vezes maior que a de todos os outros planetas somados. Sua Grande Mancha Vermelha é uma tempestade maior que a Terra, observada há mais de 150 anos. Vênus é o planeta mais quente, com temperatura superficial de cerca de 460 °C, mesmo não sendo o mais próximo do Sol: o motivo é o efeito estufa extremo causado por sua atmosfera densa de dióxido de carbono.

A distância média entre a Terra e o Sol, cerca de 149,6 milhões de quilômetros, é chamada de Unidade Astronômica (UA). A luz do Sol leva aproximadamente 8 minutos e 20 segundos para chegar até nós. A sonda Voyager 1, lançada em 1977, entrou no espaço interestelar em 2012 e é o objeto feito pelo ser humano mais distante da Terra.

## Criptografia

Criptografia é o estudo de técnicas para proteger informações, de modo que apenas quem tem a chave correta consiga lê-las. Ela se divide em duas grandes famílias.

Na criptografia simétrica, a mesma chave é usada para cifrar e decifrar. É rápida e usada para grandes volumes de dados. O padrão mais usado é o AES (Advanced Encryption Standard), baseado no algoritmo Rijndael, dos belgas Joan Daemen e Vincent Rijmen, e adotado pelo NIST (instituto de padrões dos Estados Unidos) em 2001. O AES trabalha com chaves de 128, 192 ou 256 bits.

Na criptografia assimétrica, ou de chave pública, cada pessoa tem um par de chaves: uma pública, que pode ser divulgada, e uma privada, que fica em segredo. O que é cifrado com a chave pública só pode ser decifrado com a privada. O conceito foi publicado por Whitfield Diffie e Martin Hellman em 1976, e o algoritmo RSA, de Ron Rivest, Adi Shamir e Leonard Adleman, surgiu em 1977. A segurança do RSA depende da dificuldade de fatorar números muito grandes.

Funções de hash, como o SHA-256, não são criptografia no sentido de cifrar e decifrar: elas transformam qualquer entrada em uma saída de tamanho fixo (256 bits, no caso), e é inviável voltar da saída para a entrada. Uma pequena mudança na entrada muda completamente o hash. Elas são usadas para verificar integridade de arquivos e para armazenar senhas, sempre combinadas com um "sal" (salt) e algoritmos lentos de propósito, como bcrypt ou Argon2.

Na prática, os dois tipos são combinados. No protocolo TLS, que protege o HTTPS, a criptografia assimétrica é usada no início da conexão para autenticar o servidor e combinar uma chave de sessão, e depois a comunicação segue com criptografia simétrica, que é muito mais rápida.

## Revolução Industrial

A Revolução Industrial começou na Inglaterra por volta de 1760 e marcou a passagem da produção artesanal para a produção mecanizada em fábricas. A Inglaterra reunia condições favoráveis: grandes reservas de carvão e ferro, capital acumulado com o comércio colonial, mão de obra disponível no campo e um sistema bancário desenvolvido.

A indústria têxtil foi a primeira a se transformar, com invenções como a lançadeira volante, de John Kay (1733), e a máquina de fiar "spinning jenny", de James Hargreaves (por volta de 1764). A máquina a vapor já existia, mas James Watt a tornou muito mais eficiente com a invenção do condensador separado, patenteado em 1769. A unidade de potência "watt" é uma homenagem a ele.

A Segunda Revolução Industrial, a partir de meados do século XIX, trouxe o aço, a eletricidade, o petróleo e a química industrial. As condições de trabalho nas fábricas eram duras, com jornadas de mais de 12 horas e trabalho infantil, o que levou ao surgimento dos sindicatos e das primeiras leis trabalhistas.

## DNS

O DNS (Domain Name System) é o sistema que traduz nomes de domínio, como "exemplo.com", em endereços IP, como 93.184.215.14. Ele funciona como uma lista telefônica distribuída da internet. Foi criado por Paul Mockapetris em 1983, descrito nas RFCs 882 e 883, para substituir um único arquivo de texto (HOSTS.TXT) que era copiado manualmente entre os computadores da rede.

A resolução de um nome segue uma hierarquia. O resolvedor consulta primeiro um servidor raiz, que indica os servidores do domínio de topo (como .com ou .br), que por sua vez indicam o servidor autoritativo do domínio, que dá a resposta final. Existem 13 identificadores de servidores raiz, nomeados de A a M, mas cada um é na verdade replicado em centenas de máquinas espalhadas pelo mundo.

Tipos de registros DNS mais comuns:
- A: associa um nome a um endereço IPv4
- AAAA: associa um nome a um endereço IPv6
- CNAME: cria um apelido de um nome para outro
- MX: indica os servidores de e-mail do domínio
- TXT: guarda textos livres, muito usados para verificação de domínio e políticas de e-mail (SPF, DKIM)
- NS: indica os servidores autoritativos do domínio

Cada registro tem um TTL (time to live), que diz por quanto tempo a resposta pode ficar em cache. Por isso, uma mudança de DNS pode levar horas para "propagar". O DNS usa normalmente a porta 53. No Brasil, os domínios .br são administrados pelo Registro.br, ligado ao NIC.br.

## Pão e fermentação

O pão é feito basicamente de farinha, água, sal e fermento. Quando a farinha de trigo é misturada com água e sovada, duas proteínas, a glutenina e a gliadina, formam o glúten: uma rede elástica que segura os gases da fermentação e dá estrutura à massa.

O fermento biológico é composto por leveduras da espécie Saccharomyces cerevisiae. Elas consomem os açúcares da farinha e produzem gás carbônico, que faz a massa crescer, e álcool, que evapora no forno. O fermento natural, também chamado de levain, é uma cultura de leveduras selvagens e bactérias láticas mantida com farinha e água. As bactérias produzem ácidos que dão o sabor levemente azedo do pão de fermentação natural.

A crosta dourada e o aroma do pão assado vêm principalmente da reação de Maillard, descrita pelo químico francês Louis-Camille Maillard em 1912. Ela acontece entre aminoácidos e açúcares sob calor intenso, geralmente acima de 140 °C, e é a mesma reação que doura a carne grelhada e o café torrado. Diferente dela, a caramelização é a quebra apenas de açúcares.

Uma fermentação longa e em temperatura baixa (na geladeira, por exemplo) desenvolve mais sabor, porque dá tempo para as enzimas quebrarem amidos e proteínas.

## Estruturas de dados e complexidade

A notação Big O descreve como o tempo ou a memória de um algoritmo crescem conforme o tamanho da entrada (n) aumenta. Ela ignora constantes e foca no comportamento para entradas grandes. O(1) é tempo constante, O(log n) é logarítmico, O(n) é linear, O(n log n) é típico de bons algoritmos de ordenação e O(n²) é quadrático.

| Estrutura | Acesso por posição | Busca | Inserção |
|---|---|---|---|
| Array | O(1) | O(n) | O(n) |
| Lista ligada | O(n) | O(n) | O(1) no início |
| Tabela hash | não se aplica | O(1) em média | O(1) em média |
| Árvore de busca balanceada | O(log n) | O(log n) | O(log n) |

Uma tabela hash usa uma função de hash para transformar a chave em uma posição de um array interno. Quando duas chaves caem na mesma posição, ocorre uma colisão, que pode ser tratada com listas encadeadas ou endereçamento aberto. No pior caso, com muitas colisões, a busca degrada para O(n).

A busca binária encontra um elemento em uma lista ordenada em O(log n), dividindo o intervalo pela metade a cada passo. Em uma lista de um milhão de itens, ela precisa de no máximo cerca de 20 comparações.

Entre os algoritmos de ordenação, o quicksort tem complexidade O(n log n) em média, mas O(n²) no pior caso. O merge sort é sempre O(n log n), mas usa memória extra. O Timsort, criado por Tim Peters em 2002, combina merge sort e insertion sort e é usado como ordenação padrão em várias linguagens. Está provado que nenhum algoritmo de ordenação baseado apenas em comparações pode ser melhor que O(n log n) no pior caso.

## DNA e genética

O DNA (ácido desoxirribonucleico) é a molécula que carrega as instruções genéticas dos seres vivos. Sua estrutura em dupla hélice foi descrita em 1953 por James Watson e Francis Crick, com base em dados de difração de raios X obtidos por Rosalind Franklin, incluindo a famosa "Foto 51". Watson, Crick e Maurice Wilkins receberam o Prêmio Nobel em 1962; Franklin havia morrido em 1958 e o Nobel não é concedido postumamente.

O DNA é formado por quatro bases nitrogenadas: adenina (A), timina (T), citosina (C) e guanina (G). Elas se pareiam sempre da mesma forma: A com T e C com G. A sequência dessas bases codifica as proteínas: cada grupo de três bases, chamado códon, corresponde a um aminoácido.

O genoma humano tem cerca de 3 bilhões de pares de bases e aproximadamente 20 mil genes que codificam proteínas, o que representa menos de 2% do total. O Projeto Genoma Humano, iniciado em 1990, anunciou a conclusão do sequenciamento em 2003. A técnica CRISPR-Cas9, desenvolvida por Jennifer Doudna e Emmanuelle Charpentier, permite editar trechos específicos do DNA e rendeu a elas o Nobel de Química de 2020.

## Redis

Redis (REmote DIctionary Server) é um banco de dados em memória do tipo chave-valor, criado pelo italiano Salvatore Sanfilippo em 2009. Por manter os dados na memória RAM, ele responde em frações de milissegundo, o que o torna muito usado como cache, armazenamento de sessões, filas e contadores em tempo real.

Além de strings simples, o Redis oferece estruturas de dados como listas, conjuntos (sets), conjuntos ordenados (sorted sets), hashes e streams. Os sorted sets, por exemplo, são ideais para rankings de jogos. Cada chave pode receber um tempo de expiração (TTL), depois do qual é apagada automaticamente.

Mesmo sendo em memória, o Redis pode persistir dados em disco de duas formas: snapshots periódicos (RDB) ou um log de todas as operações de escrita (AOF). A execução dos comandos acontece em uma única thread principal, o que garante que cada comando seja atômico. A porta padrão é a 6379. Em 2024, o Redis mudou sua licença, e a Linux Foundation lançou um fork de código aberto chamado Valkey.

## Copa do Mundo

A Copa do Mundo da FIFA é o principal torneio de seleções de futebol, disputado a cada quatro anos. A primeira edição foi em 1930, no Uruguai, e o próprio Uruguai foi campeão ao vencer a Argentina na final. As edições de 1942 e 1946 não aconteceram por causa da Segunda Guerra Mundial.

O Brasil é o maior campeão, com cinco títulos: 1958 (Suécia), 1962 (Chile), 1970 (México), 1994 (Estados Unidos) e 2002 (Coreia do Sul e Japão). Pelé é o único jogador a ter vencido três Copas, em 1958, 1962 e 1970. O Brasil também é a única seleção que participou de todas as edições.

A Copa de 1950, no Brasil, terminou com a derrota brasileira para o Uruguai por 2 a 1 no Maracanã, episódio conhecido como "Maracanazo". A Copa de 2022, no Catar, foi vencida pela Argentina de Lionel Messi, nos pênaltis, contra a França. A edição de 2026, sediada por Estados Unidos, Canadá e México, foi a primeira com 48 seleções.

## Testes de software

Testes automatizados verificam se o código se comporta como esperado e permitem fazer mudanças com segurança. A pirâmide de testes, popularizada por Mike Cohn, sugere ter muitos testes unitários na base, uma quantidade menor de testes de integração no meio e poucos testes de ponta a ponta (end-to-end) no topo, porque estes últimos são mais lentos e frágeis.

- Teste unitário: testa uma função ou classe isolada, geralmente em milissegundos.
- Teste de integração: testa a comunicação entre partes, como o código e um banco de dados real.
- Teste end-to-end: simula o usuário usando o sistema completo, por exemplo clicando em um navegador.

Quando uma dependência externa é difícil de usar nos testes, ela pode ser substituída por um dublê de teste. Um "mock" é um dublê que também verifica como foi chamado; um "stub" apenas devolve respostas pré-definidas.

O TDD (Test-Driven Development), sistematizado por Kent Beck no início dos anos 2000, propõe escrever o teste antes do código, em um ciclo de três passos chamado vermelho-verde-refatorar: escreve-se um teste que falha (vermelho), depois o código mínimo para ele passar (verde) e por fim melhora-se o código mantendo os testes passando (refatorar).

A cobertura de testes mede a porcentagem de linhas executadas pelos testes. Uma cobertura alta não garante que os testes sejam bons: um teste pode executar uma linha sem verificar nada sobre o resultado.

## Inflação e o Plano Real

Inflação é o aumento generalizado e contínuo dos preços, que reduz o poder de compra da moeda. No Brasil, o índice oficial é o IPCA (Índice Nacional de Preços ao Consumidor Amplo), calculado mensalmente pelo IBGE.

O Brasil adota desde 1999 o regime de metas de inflação. O Conselho Monetário Nacional (CMN) define a meta, e o Comitê de Política Monetária (Copom) do Banco Central, que se reúne oito vezes por ano, define a taxa básica de juros, a Selic, para tentar alcançá-la. Juros mais altos encarecem o crédito, reduzem o consumo e ajudam a segurar os preços.

Entre o fim dos anos 1980 e o início dos anos 1990, o país viveu hiperinflação, com taxas acima de 80% ao mês em alguns momentos. Vários planos econômicos fracassaram, como o Plano Cruzado (1986) e o Plano Collor (1990). O Plano Real, de 1994, teve sucesso usando uma transição em etapas: primeiro foi criada a URV (Unidade Real de Valor), em março, uma unidade de conta que acompanhava a inflação diariamente; depois, em 1º de julho de 1994, a URV foi convertida na nova moeda, o real.

## Mensageria

Sistemas de mensageria permitem que partes de uma aplicação se comuniquem de forma assíncrona: quem envia a mensagem (produtor) não precisa esperar quem a processa (consumidor). Isso desacopla serviços e absorve picos de carga, já que as mensagens ficam guardadas até serem processadas.

Há dois modelos principais. Na fila (ponto a ponto), cada mensagem é entregue a um único consumidor. No publish/subscribe (pub/sub), uma mensagem publicada em um tópico é entregue a todos os assinantes daquele tópico.

O RabbitMQ, lançado em 2007 e escrito em Erlang, é um broker de mensagens que implementa o protocolo AMQP. Ele roteia mensagens por meio de "exchanges" para filas, e a mensagem normalmente é removida depois de confirmada pelo consumidor.

O Apache Kafka foi criado no LinkedIn, liberado como código aberto em 2011, e recebeu o nome em homenagem ao escritor Franz Kafka. Ele funciona como um log distribuído: as mensagens são gravadas em ordem em partições de um tópico e ficam armazenadas por um período configurável, mesmo depois de lidas. Cada consumidor controla sua posição no log, chamada offset, o que permite reprocessar mensagens antigas. Consumidores de um mesmo grupo dividem as partições entre si para processar em paralelo.

Uma garantia comum é a entrega "pelo menos uma vez" (at-least-once), em que uma mensagem pode chegar duplicada. Por isso, os consumidores devem ser idempotentes: processar a mesma mensagem duas vezes deve ter o mesmo efeito que processá-la uma vez.

## Teoria musical

A música ocidental usa 12 notas na escala cromática: dó, dó sustenido, ré, ré sustenido, mi, fá, fá sustenido, sol, sol sustenido, lá, lá sustenido e si. A distância entre duas notas vizinhas é um semitom; dois semitons formam um tom.

A escala maior segue o padrão tom, tom, semitom, tom, tom, tom, semitom. A partir de dó, isso resulta em dó, ré, mi, fá, sol, lá, si e dó, sem nenhuma tecla preta no piano.

O som é uma vibração, e a altura de uma nota depende da sua frequência. A nota lá central é padronizada em 440 Hz. Subir uma oitava significa dobrar a frequência: o lá seguinte tem 880 Hz. No sistema de temperamento igual, usado na maioria dos instrumentos modernos, a oitava é dividida em 12 semitons iguais, e cada semitom multiplica a frequência pela raiz duodécima de 2, aproximadamente 1,0595.

Um acorde é a combinação de três ou mais notas tocadas juntas. O acorde maior é formado pela tônica, a terça maior e a quinta justa (dó, mi e sol no caso de dó maior) e costuma soar "alegre". O acorde menor troca a terça maior pela terça menor (dó, mi bemol e sol) e costuma soar "triste".

## Unicode e UTF-8

Computadores guardam texto como números. A tabela ASCII, de 1963, usa 7 bits e define 128 caracteres: letras sem acento, dígitos, pontuação e caracteres de controle. Ela não tem "ç" nem "ã", o que levou à criação de várias tabelas estendidas incompatíveis entre si, como a ISO-8859-1 (Latin-1) e a Windows-1252. Um texto salvo em uma e lido em outra aparece com caracteres trocados, como "Ã§" no lugar de "ç".

O Unicode resolve esse problema atribuindo um número único, chamado ponto de código, a cada caractere de todos os sistemas de escrita, além de símbolos e emojis. O "A" é U+0041 e o "ç" é U+00E7. A primeira versão foi publicada em 1991, e hoje o padrão tem mais de 150 mil caracteres.

O Unicode define os números, mas não como eles são gravados em bytes; isso é papel da codificação. A UTF-8, criada por Ken Thompson e Rob Pike em 1992, usa de 1 a 4 bytes por caractere. Os caracteres ASCII ocupam 1 byte, exatamente como antes, o que torna a UTF-8 compatível com ASCII. Letras acentuadas usam 2 bytes e a maioria dos emojis usa 4. A UTF-8 é usada em mais de 98% das páginas da web.

## Amazônia

A Floresta Amazônica é a maior floresta tropical do mundo, com cerca de 5,5 milhões de quilômetros quadrados. Cerca de 60% dela fica no Brasil, e o restante se distribui por Peru, Colômbia, Venezuela, Equador, Bolívia, Guiana, Suriname e Guiana Francesa.

O rio Amazonas é o maior do mundo em volume de água, responsável por cerca de 20% de toda a água doce que os rios despejam nos oceanos. Em Manaus, ocorre o Encontro das Águas: o rio Negro, escuro, e o rio Solimões, barrento, correm lado a lado por vários quilômetros sem se misturar, por diferenças de temperatura, velocidade e densidade.

A floresta abriga uma das maiores biodiversidades do planeta e influencia o clima de outras regiões. Os chamados "rios voadores" são correntes de umidade que saem da Amazônia pela evaporação e transpiração das árvores e levam chuva para o Centro-Oeste e o Sudeste do Brasil. O desmatamento é monitorado por satélite pelo INPE, por meio dos sistemas PRODES e DETER.

## Teorema CAP

O teorema CAP afirma que um sistema de dados distribuído não consegue garantir ao mesmo tempo as três propriedades a seguir:
- Consistência (Consistency): toda leitura recebe a escrita mais recente.
- Disponibilidade (Availability): toda requisição recebe uma resposta, sem erro.
- Tolerância a partição (Partition tolerance): o sistema continua funcionando mesmo que a rede entre os nós falhe.

A ideia foi apresentada como conjectura por Eric Brewer em 2000 e provada formalmente por Seth Gilbert e Nancy Lynch em 2002.

Como falhas de rede são inevitáveis em sistemas distribuídos reais, a escolha prática acontece durante uma partição: o sistema deve escolher entre consistência (recusar requisições até a rede voltar) ou disponibilidade (responder, mesmo com dados possivelmente desatualizados). Sistemas que priorizam disponibilidade costumam oferecer consistência eventual: se as escritas pararem, todos os nós acabam convergindo para o mesmo valor.

O modelo PACELC, proposto por Daniel Abadi, complementa o CAP: se há partição (P), escolhe-se entre disponibilidade (A) e consistência (C); senão (E, de "else"), escolhe-se entre latência (L) e consistência (C).

## Café

Segundo a lenda, o café foi descoberto na Etiópia por um pastor chamado Kaldi, que percebeu que suas cabras ficavam agitadas depois de comer os frutos de um certo arbusto. Os primeiros registros confiáveis do consumo da bebida são do século XV, em mosteiros sufis do Iêmen.

O café chegou ao Brasil em 1727, quando o sargento-mor Francisco de Melo Palheta trouxe mudas da Guiana Francesa para o Pará. No século XIX, o cultivo se expandiu pelo Vale do Paraíba e depois pelo oeste paulista, e o café se tornou o principal produto de exportação do país. O Brasil é o maior produtor mundial há mais de 150 anos.

As duas espécies mais cultivadas são a Coffea arabica (arábica), de sabor mais suave e complexo, e a Coffea canephora (conhecida como robusta ou conilon), mais amarga e com mais cafeína. Na torra, a reação de Maillard e a caramelização desenvolvem centenas de compostos aromáticos.

A cafeína tem efeito estimulante porque bloqueia os receptores de adenosina no cérebro. A adenosina se acumula ao longo do dia e provoca a sensação de cansaço; com os receptores bloqueados, essa sensação diminui.

## OAuth 2.0 e JWT

O OAuth 2.0 é um protocolo de autorização, publicado como RFC 6749 em 2012. Ele permite que um aplicativo acesse recursos de um usuário em outro serviço sem conhecer a senha dele. É o que acontece quando um site pede "Entrar com o Google" e mostra uma tela perguntando quais permissões você concede.

Os papéis envolvidos são: o dono do recurso (o usuário), o cliente (o aplicativo que quer o acesso), o servidor de autorização (que autentica o usuário e emite tokens) e o servidor de recursos (a API que guarda os dados). O fluxo mais recomendado para aplicativos com usuário é o Authorization Code com PKCE. Para comunicação entre servidores, sem usuário, usa-se o fluxo Client Credentials.

O resultado do fluxo é um access token, de vida curta, enviado nas requisições no cabeçalho "Authorization: Bearer <token>", e frequentemente um refresh token, de vida longa, usado para obter novos access tokens sem pedir login de novo. O OpenID Connect é uma camada sobre o OAuth 2.0 que adiciona autenticação, ou seja, informa quem é o usuário.

O JWT (JSON Web Token), definido na RFC 7519 de 2015, é um formato comum para tokens. Ele tem três partes separadas por pontos: cabeçalho, payload e assinatura, cada uma codificada em Base64URL. A assinatura, feita com algoritmos como HS256 (chave secreta compartilhada) ou RS256 (par de chaves RSA), garante que o token não foi alterado. Atenção: o payload de um JWT assinado não é cifrado; qualquer pessoa pode decodificá-lo e lê-lo, então ele nunca deve conter senhas ou dados sigilosos.

## Relatividade

Albert Einstein publicou a teoria da relatividade restrita em 1905, ano conhecido como seu "ano milagroso", no qual também publicou trabalhos sobre o efeito fotoelétrico e o movimento browniano. A teoria parte de dois postulados: as leis da física são as mesmas para todos os observadores em movimento uniforme, e a velocidade da luz no vácuo é a mesma para todos eles, exatamente 299.792.458 metros por segundo.

Consequências da relatividade restrita incluem a dilatação do tempo (relógios em movimento andam mais devagar), a contração do comprimento e a equivalência entre massa e energia, expressa na equação E = mc².

A relatividade geral, apresentada em 1915, descreve a gravidade não como uma força, mas como a curvatura do espaço-tempo causada pela massa e pela energia. Uma de suas previsões, o desvio da luz das estrelas ao passar perto do Sol, foi confirmada durante o eclipse solar de 29 de maio de 1919, com observações feitas em Sobral, no Ceará, e na ilha de Príncipe, na África. Em 2015, o observatório LIGO detectou pela primeira vez ondas gravitacionais, outra previsão da teoria.

O GPS precisa levar a relatividade em conta. Os relógios dos satélites andam mais rápido que os da Terra por estarem em um campo gravitacional mais fraco (efeito da relatividade geral) e mais devagar por estarem em movimento (efeito da relatividade restrita). O saldo é um adiantamento de cerca de 38 microssegundos por dia, que, se não fosse corrigido, geraria erros de posição de cerca de 10 quilômetros por dia.

## Expressões regulares

Expressões regulares (regex) são padrões usados para buscar e manipular texto. A base teórica vem dos "conjuntos regulares" descritos pelo matemático Stephen Kleene na década de 1950. Ken Thompson as levou para a computação no fim dos anos 1960, nos editores QED e ed. O nome do comando grep vem do comando do ed "g/re/p" (global, regular expression, print).

Metacaracteres mais usados:
- . qualquer caractere (exceto quebra de linha)
- * zero ou mais repetições; + uma ou mais; ? zero ou uma
- ^ início da linha; $ fim da linha
- [abc] qualquer um dos caracteres listados; [^abc] qualquer um exceto eles
- \d dígito; \w caractere de palavra; \s espaço em branco
- ( ) agrupa e captura; | significa "ou"
- {2,4} entre duas e quatro repetições

Exemplos:

```
^\d{5}-\d{3}$          CEP no formato 01310-100
^[\w.+-]+@[\w-]+\.[\w.]+$   e-mail (versão simplificada)
\b(19|20)\d{2}\b       anos entre 1900 e 2099
```

Por padrão, os quantificadores são gulosos (greedy): tentam casar o máximo possível. No texto "<a><b>", o padrão "<.*>" casa a string inteira, enquanto a versão preguiçosa (lazy) "<.*?>" casa só "<a>".

Expressões mal construídas podem causar backtracking catastrófico, em que o tempo de execução cresce exponencialmente com o tamanho da entrada. Em julho de 2019, uma única regex desse tipo levou a CPU dos servidores da Cloudflare a 100% e derrubou boa parte dos sites atendidos pela empresa por cerca de meia hora. Esse tipo de ataque é chamado de ReDoS.

## Xadrez

O xadrez é jogado em um tabuleiro de 64 casas, com 16 peças para cada jogador: um rei, uma dama, duas torres, dois bispos, dois cavalos e oito peões. O objetivo é dar xeque-mate, ou seja, atacar o rei adversário de forma que ele não tenha como escapar. O jogo tem origem no chaturanga, da Índia, por volta do século VI.

Valores tradicionais aproximados das peças: peão vale 1, cavalo e bispo valem 3, torre vale 5 e dama vale 9. O rei não tem valor, porque perdê-lo é perder a partida. Jogadas especiais incluem o roque, a promoção do peão e a captura en passant.

O matemático Claude Shannon estimou, em 1950, que o número de partidas possíveis seria da ordem de 10 elevado a 120, número conhecido como "número de Shannon" e muito maior que a quantidade estimada de átomos no universo observável.

Em 1997, o computador Deep Blue, da IBM, venceu o campeão mundial Garry Kasparov em um match de seis partidas, por 3,5 a 2,5. Em 2017, o AlphaZero, da DeepMind, aprendeu a jogar apenas jogando contra si mesmo, sem nenhuma partida humana como exemplo, e em poucas horas de treinamento derrotou o Stockfish, um dos motores de xadrez mais fortes da época.
