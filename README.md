## Requisitos para executar o proejeto 

1. Ter o docker instalado;
2. Ter python(Selenium, Tabula, Flask), o Vue.js e o Node instalados;
3. Criar um arquivo .env e preencher as seguintes informações:
   
        URL=
        DOWNLOAD_DIR=
        ROOT_PASSWORD=
        DATABASE_NAME=
        USER_LOGIN=
        USER_PASSWORD=
        START_DB_PATH=
        PORTS=
        CONTAINER_NAME=

## Informações extras e justificativas de implementação:

- A arquitetura escolhida, apesar de ser mais complexa do que o necessário para essa simples aplicação foi pensada graças a escalabilidade (existem até alguns serviços prontos que não chegaram a ser criados na camada de aplicação);
- A razão de rodar apenas o banco pelo docker, ao invés de toda a aplicação, foi devido ao tamanho da imagem;
- A criação dos indexs no banco, além da escolha por views ao invés de querys simples estão diretamente relacionadas à quantidade de dados (especialmente os da tabela de contabilidade que ultrapassam as 7 milhões de linhas);
- A utilização por ids simples ao invés de UUIDs se dá devido ao caráter simplificado e o propósito sem prático da aplicação (apesar de poder ser utilizada);
- A normalização dos dados advindos dos arquivos csv foi simplificada, como não houve especificações, fiz apenas mudanças pontuais para que não ficasse uma bagunça (Imagino que para esses dados, uma modelagem dimensional seria mais recomendada);
- Foi criada uma pequena coleção no postman que testa 3 casos simples de uso (https://carloseduardo-2179910.postman.co/workspace/Carlos-Eduardo's-Workspace~f8b1c3f6-b4d7-4988-8532-b22c184c0e8e/collection/43572967-c7ae0cc3-264c-46e4-8ca4-4a40bf948e7d?action=share&creator=43572967).
- **MAIS DETALHES SOBRE A LÓGICA IMPLANTADA, REQUISITOS, ETC; PODEM SER CONFERIDOS A PARTIR DO HISTÓRICO DE BRANCHS, COMMITS, ISSUES E PRs**
