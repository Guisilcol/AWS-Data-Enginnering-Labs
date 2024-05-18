# AWS Data Engineering Lab

Este repositório contém o ambiente que será usado durante o laboratório intensivo para aprender e praticar habilidades de engenharia de dados usando AWS. O laboratório cobre uma ampla gama de tópicos, incluindo ingestão de dados, APIs, streaming, bancos de dados, cloud, data lakehouse e muito mais.

## Estrutura do Repositório

### Diretórios e Arquivos

- **datalake/**: Scripts, jobs e conteúdo geral para atender o datalake.
- **docker_assets/**: Recursos Docker necessários para o laboratório, incluindo subdiretórios como `api` e `db`.
- **Makefile**: Automação de tarefas para construir e gerenciar a infraestrutura e ambientes de desenvolvimento.
- **Makefile.win**: Versão do Makefile adaptada para ambiente Windows.
- **Timeline.md**: Documento descrevendo o conteúdo e o cronograma do treinamento.
- **docker-compose.yaml**: Configuração Docker Compose para orquestrar serviços Docker necessários para o laboratório.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados e configurados antes de iniciar o laboratório:

- **Docker**: Ferramenta de virtualização que permite criar contêineres.
  - [Instalação do Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Ferramenta para definir e gerenciar multi-contêineres Docker.
  - [Instalação do Docker Compose](https://docs.docker.com/compose/install/)
- **Make**: Ferramenta de automação de tarefas.
  - [Instalação do Make](https://www.gnu.org/software/make/)
- **Visual Studio Code (VSCode)**: Editor de código-fonte leve e poderoso. Instalar as extensões `Dev Containers`, `Docker` e `Python` da Microsoft. Lembre-se que, uma vez que estiver usando Dev Containers, é provável que você precise instalar as mesmas extensões citadas dentro do Dev Container. 
  - [Download do VSCode](https://code.visualstudio.com/)

## Visão Geral do Laboratório

Este laboratório é um treinamento intensivo que abrange vários aspectos fundamentais da engenharia de dados, utilizando uma ampla gama de tecnologias e ferramentas modernas. O conteúdo é estruturado para fornecer uma experiência prática e aprofundada em diversas áreas, conforme descrito abaixo:

### Conteúdos do Treinamento
- **Ingestão de Dados**: Coleta e ingestão de dados de várias fontes, incluindo APIs, tópicos Kafka e bancos de dados relacionais.
- **Engenharia de Software**: Conceitos e práticas necessárias para desenvolver soluções de engenharia de dados robustas. 
- **Python**: Programação em Python para manipulação e processamento de dados.
- **AWS**: Utilização de serviços AWS, incluindo S3, Glue, Lambda, Athena, Step Functions e IAM para armazenamento, processamento e gestão de dados na nuvem.
- **Kafka** (Streaming): Processamento de dados em tempo real usando Kafka.
- **SQL**: Manipulação e consulta de dados utilizando SQL.
- **API**: Desenvolvimento e consumo de APIs para acesso e manipulação de dados.
- **Modelagem Dimensional**: Técnicas de modelagem de dados para data warehouses.
- **Arquitetura de Soluções no Cloud**: Desenvolvimento de arquiteturas de dados escaláveis e eficientes na nuvem.
- **Spark**: Processamento distribuído de grandes volumes de dados com Apache Spark.
- **Terraform**: Automação da infraestrutura como código usando Terraform.
- **Docker**: Contêinerização e orquestração de aplicações com Docker.
- **Implementação de um Data Lakehouse na AWS**: Integração de data lakes e data warehouses para gerenciamento de dados em grande escala.
- **Governança de Dados**: Práticas e políticas para garantir a qualidade e segurança dos dados.
- **ETL**: Extração, transformação e carga de dados.
- **Orquestração de Jobs**: Automatização e gerenciamento de workflows de dados.

## Configuração e Execução

Uma vez que você tenha instalado os pré-requisitos acima e clonado este repositório, poderá utilizar o projeto de imediato. Para isso, siga as instruções abaixo:

1. Caso o seu sistema operacional seja Windows, renomeie o arquivo `Makefile.win` para `Makefile`.
2. Usando o utilitário `make`, execute o comando `make start-source-infra` para iniciar os serviços Docker que serão usados como fontes de dados.
3. Certifique-se de que os serviços estão em execução corretamente, verificando os logs dos contêineres.
4. Execute o comando `make start-dev-container` para iniciar um ambiente de desenvolvimento com todas as ferramentas necessárias.
5. Utilizando a extensão `Dev Containers` do VSCode, acesse o Dev Container chamado `aws_labs_dev_container` e abra a pasta `/workspace` para começar a trabalhar. Essa pasta é compartilhada com o ambiente Docker, referenciando o código local no seu computador.
6. Uma vez dentro do Dev Container, execute o comando `create-venvs` para fazer a criação dos ambientes virtuais Python. 
7. A partir desse ponto, você pode começar a explorar e executar os scripts e códigos de exemplo fornecidos no laboratório. Não se esqueça de mudar o ambiente virtual Python utilizado no canto inferior direito do VSCode: isso é importante porque para cada serviço (lambda, glue Python Shell e Glue Spark) é necessário um ambiente virtual Python específico.