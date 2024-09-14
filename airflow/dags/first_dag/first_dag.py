
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import pprint


def p_codigo(**kwargs):
    print("f python")
    pprint.pprint(kwargs)
    return 123

with DAG(
    dag_id = "a_first_dag",
    start_date = datetime(2024, 9 , 1),
    schedule = "@daily",
    doc_md = __doc__
):
    start = EmptyOperator(task_id = "start")
    python = PythonOperator(task_id = "python", python_callable=p_codigo)
    end = EmptyOperator(task_id = "end")
    
start >> python >> end
