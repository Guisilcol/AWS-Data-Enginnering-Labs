
Conteúdos do treinamento
========================

- Ingestão de dados 
- Python 
- AWS (S3, Glue, Lambda, Athena, Step Functions, IAM)
- Kafka (Streaming)
- SQL 
- API 
- Modelagem Dimensional
- Arquitetura de soluções no Cloud
- Spark 
- Terraform 
- Docker 
- Implementação de um Data Lakehouse na AWS 
- Governança de dados
- ETL 
- Orquestração de jobs

Cronograma
==========

- Introdução do treinamento -> 1h 
- Configuração das estações de trabalho -> 3h 
- Testes iniciais dos ambientes -> 1h
- Introdução aos projetos de ingestão de dados -> 3h
- Desenvolvimento de um projeto de ingestão de dados em grupo -> 4h
- Desenvolvimento de um projeto de ingestão de dados individual -> 40h 
- Introdução à arquitetura de soluções no Cloud -> 4h 
- Desenvolvimento da arquitetura de uma solução Lakehouse no Cloud -> 40h 
- Introdução à governança de dados -> 2h 
- Implementação da fundação do Lakehouse  -> 16h 
- Desenvolvimento das cargas nas camadas bronze e silver -> 40h 
- Levantamento das regras de carga da camada gold -> 16h 
- Modelagem dimensional na camada gold -> 16h
- Desenvolvimento as cargas na camada gold -> 40h
- Introdução ao Terraform -> 2h 
- Desenvolvimento de um projeto de automatização de deploy de jobs Lambdas e Glue em grupo -> 6h 
- Desenvolvimento de um projeto de automatização de deploy de jobs Lambdas e Glue individual -> 40h

Total de horas: 274

Justificativa para a Instalação de Docker e WSL nos Desktops do Treinamento de Engenharia de Dados
==================================================================================================

Para garantir a eficiência do treinamento de engenharia de dados que será ministrado, é essencial que os desktops disponibilizados estejam equipados com os softwares Windows Subsystem for Linux (WSL) e Docker. 

1. Ingestão de Dados
Execução em Containers: Todas as origens de dados que utilizaremos na etapa de ingestão serão executadas em containers. Isso garante um ambiente controlado e replicável, essencial para a consistência do treinamento.

2. Desenvolvimento, Codificação e Deploy
Dev Container da AWS: Utilizaremos um Dev Container baseado na imagem disponibilizada no Docker Hub pela AWS. Essa imagem permite que possamos codificar e executar códigos utilizando as bibliotecas do AWS Glue, garantindo que todos os participantes tenham acesso às mesmas ferramentas e versões.
Ferramentas Necessárias: O container incluirá todos os softwares necessários para as diversas etapas do treinamento, tais como Make, Terraform, AWS CLI, Git, entre outros. Isso assegura que o ambiente de desenvolvimento esteja completo e pronto para uso, sem necessidade de instalações adicionais.

3. Performance e Viabilidade
Importância do WSL para Docker: Embora seja possível executar Docker sem o WSL, a performance é significativamente inferior, tornando o uso inviável. Testes realizados nas máquinas pessoais do Guilherme mostraram que, com o uso do Docker em conjunto com o WSL, a performance foi superior, permitindo um uso eficiente dos containers.

