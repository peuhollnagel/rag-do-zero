# Docker

Docker é uma plataforma de conteinerização lançada em 2013 pela empresa dotCloud, que depois mudou seu nome para Docker Inc.

Um contêiner empacota uma aplicação junto com todas as suas dependências (bibliotecas, configurações, runtime), garantindo que ela rode da mesma forma em qualquer ambiente. Contêineres são mais leves que máquinas virtuais porque compartilham o kernel do sistema operacional hospedeiro, em vez de emular um sistema completo.

Conceitos principais:
- Imagem: um modelo somente leitura usado para criar contêineres
- Dockerfile: arquivo de texto com as instruções para construir uma imagem
- Contêiner: uma instância em execução de uma imagem
- Docker Hub: registro público onde imagens são compartilhadas
- Docker Compose: ferramenta para definir e rodar aplicações com vários contêineres usando um arquivo YAML

O Docker se tornou peça central em práticas de DevOps e microsserviços, frequentemente orquestrado pelo Kubernetes em produção.
