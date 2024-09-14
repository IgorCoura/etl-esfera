
from airflow import DAG

from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

from etl_sp_budget.etl_sp_budget_scripts.extract_data import ExtractData
from etl_sp_budget.etl_sp_budget_scripts.transform_data import TransformData
from etl_sp_budget.etl_sp_budget_scripts.load_data import LoadData
from etl_sp_budget.etl_sp_budget_scripts.sql_scripts import CREATE_TABLES
from airflow.models import Variable

def extract(**kwargs):
    url_expenses = Variable.get("url_expenses")
    url_revenue = Variable.get("url_revenue")
    expenses = ExtractData.get_data(url_expenses)
    kwargs['ti'].xcom_push(key="expenses", value =expenses)
    revenue = ExtractData.get_data(url_revenue)
    kwargs['ti'].xcom_push(key="revenue", value =revenue)
    

def transform(**kwargs):
    expenses = kwargs['ti'].xcom_pull(task_ids='extract', key = "expenses")
    revenue = kwargs['ti'].xcom_pull(task_ids='extract', key= "revenue")
    result = TransformData.transform_resources(expenses, True, True)
    result.extend(TransformData.transform_resources(revenue, False, True))
    return result

def load(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='transform')
    hook = PostgresHook(postgres_conn_id="etl-sp-budget-db", schema="etl_sp_budget_db")
    connection = hook.get_conn()
    loader = LoadData(connection)
    loader.load_all_resources(data)

with DAG(
    dag_id = "a_etl_sp_buget",
    start_date = datetime(2024, 9 , 1),
    schedule = "@daily",
):
    start = EmptyOperator(task_id = "start")
    extract = PythonOperator(task_id = "extract", python_callable=extract)
    transform = PythonOperator(task_id = "transform", python_callable=transform)
    create_tables = PostgresOperator(task_id="create_tables", postgres_conn_id="etl-sp-budget-db", sql=CREATE_TABLES)
    load = PythonOperator(task_id = "load", python_callable=load)
    end = EmptyOperator(task_id = "end")
    
start >> extract >> transform  >> create_tables >> load >> end
