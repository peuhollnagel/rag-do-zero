# Kubernetes

Kubernetes, também chamado de K8s, é um sistema de código aberto para orquestração de contêineres. Foi criado pelo Google com base em seu sistema interno chamado Borg e doado à Cloud Native Computing Foundation (CNCF) em 2015.

O "8" em K8s representa as oito letras entre o "K" e o "s" da palavra Kubernetes, que vem do grego e significa "timoneiro" ou "piloto".

Componentes e conceitos:
- Pod: a menor unidade implantável, contendo um ou mais contêineres
- Node: uma máquina (física ou virtual) que executa pods
- Cluster: conjunto de nodes gerenciados por um plano de controle
- Deployment: define o estado desejado de uma aplicação, como o número de réplicas
- Service: expõe um conjunto de pods através de um endereço de rede estável
- kubectl: ferramenta de linha de comando para interagir com o cluster

O Kubernetes oferece escalonamento automático, autorrecuperação (reinicia contêineres que falham) e atualizações sem tempo de inatividade (rolling updates).
