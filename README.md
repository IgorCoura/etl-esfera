# ETL e Análise do Orçamento de São Paulo

Este projeto realiza o **ETL** (Extração, Transformação e Carga) de dados do Orçamento de São Paulo, disponíveis em arquivos CSV, seguido de uma análise utilizando um dashboard interativo.

## Requisitos

- Docker
- Docker Compose
- Power Bi

## Execução do ETL

### Passos para execução:

1. Suba os containers usando o comando:
    ```bash
    docker-compose up
    ```
   Esse comando deve ser executado a partir do arquivo `docker-compose.yaml` contido na pasta `airflow`.

2. Acesse a interface do Airflow:
    - URL: `localhost:8080`
    - Usuário: `airflow`
    - Senha: `airflow`

3. Defina as variáveis no Airflow em **Admin > Variables**:
    - `url_expenses` : `https://github.com/IgorCoura/etl-esfera/raw/main/data/gdvDespesasExcel.csv`
    - `url_revenue` : `https://github.com/IgorCoura/etl-esfera/raw/main/data/gdvReceitasExcel.csv`

4. Execute manualmente a DAG `a_etl_sp_budget`.

5. Os resultados do ETL serão armazenados no banco de dados Postgres:
    - Host: `localhost:50001`
    - Banco de dados: `etl_sp_budget_db`
    - Usuário: `admin`
    - Senha: `admin`

## Dashboard

Para visualizar os dados no dashboard:

1. Abra o arquivo `dashboard.pbix` no Power BI.
2. Conecte-se ao banco de dados Postgres configurado anteriormente.
3. Atualize os dados diretamente no Power BI.
