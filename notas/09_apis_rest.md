# APIs REST

REST (Representational State Transfer) é um estilo de arquitetura para sistemas distribuídos, definido por Roy Fielding em sua tese de doutorado no ano 2000. APIs que seguem esses princípios são chamadas de APIs RESTful.

Uma API REST expõe recursos através de URLs e usa os métodos do protocolo HTTP para operar sobre eles:
- GET: busca um recurso
- POST: cria um novo recurso
- PUT: substitui um recurso existente
- PATCH: atualiza parcialmente um recurso
- DELETE: remove um recurso

Um princípio importante do REST é ser stateless (sem estado): cada requisição deve conter todas as informações necessárias, sem depender de sessões guardadas no servidor.

As respostas usam códigos de status HTTP: 200 (OK), 201 (Criado), 400 (Requisição inválida), 401 (Não autenticado), 403 (Proibido), 404 (Não encontrado) e 500 (Erro interno do servidor). O formato de dados mais usado é o JSON. Alternativas ao REST incluem GraphQL, criado pelo Facebook, e gRPC, criado pelo Google.
