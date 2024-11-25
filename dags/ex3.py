from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'etl')))
from extract import get_recall_data
from transform import transform_data
from load import load_data_to_s3, AWS_S3_BUCKET_NAME
NAME_FOR_S3='e3/recalls_cleaned.csv'
raw_url = 'http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ex3_dag',
    default_args=default_args,
    description='A simple DAG for ex3.py',
    schedule_interval=timedelta(minutes=3),
)

def extract_data(**kwargs):
    data = get_recall_data(raw_url)
    kwargs['ti'].xcom_push(key='raw_data', value=data)

def transform_data_task(**kwargs):
    ti = kwargs['ti']
    raw_data = ti.xcom_pull(key='raw_data', task_ids='extract_data')
    transformed_data = transform_data(raw_data)
    ti.xcom_push(key='transformed_data', value=transformed_data)

def load_data_task(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(key='transformed_data', task_ids='transform_data')
    load_data_to_s3(transformed_data, AWS_S3_BUCKET_NAME, NAME_FOR_S3 )

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    provide_context=True,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data_task,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data_task,
    provide_context=True,
    dag=dag,
)

extract_task >> transform_task >> load_task

# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'etl'))
# from extract import get_recall_data
# from transform import transform_data
# from load import load_data_to_s3, AWS_S3_BUCKET_NAME, NAME_FOR_S3
# def main():
#     url = 'http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh'
#     data = get_recall_data(url)
#     if data:
#         transformed_data = transform_data(data)
#         load_data_to_s3(transformed_data, AWS_S3_BUCKET_NAME, NAME_FOR_S3)

# if __name__ == "__main__":
#     main()