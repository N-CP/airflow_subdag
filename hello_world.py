import airflow
from datetime import datetime , timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.subdag_operator import SubDagOperator
from hello_world_target import sub_dag
from airflow.utils.trigger_rule import TriggerRule

dag = DAG('hello_world',
          schedule_interval='@daily',
          start_date=datetime(2017, 12, 9), catchup=False)


t1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Hello World from Task 1"',
    dag=dag)

t2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Hello World from Task 2"',
    dag=dag)

t3 = SubDagOperator(
    subdag=sub_dag,
    task_id='task_3',
    bash_command='echo "Hello World from Task 3"',
    dag=dag,
    trigger_rule=TriggerRule.ALL_DONE)
	

t4 = BashOperator(
    task_id='task_4',
    bash_command='echo "Hello World from Task 4"',
    dag=dag)

t5 = BashOperator(
    task_id='task_5',
    bash_command='echo "Hello World from Task 5"',
    dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t4)