import airflow
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from datetime import datetime,timedelta

args = {
    'start_date': datetime(2017, 12, 9),
    'owner': 'airflow',
}

sub_dag = DAG('hello_world.task_3',
         default_args=args,
          schedule_interval='@daily')

t1 = BashOperator(
    task_id='task1',
    bash_command='echo "Hello World from Task 1"',
    dag=sub_dag)

t2 = BashOperator(
    task_id='task2',
    bash_command='echo "Hello World from Task 2"',
    dag=sub_dag)

t3 = BashOperator(
     task_id='task3',
     bash_command='echo "Hello World from Task 3"',
     dag=sub_dag)

t4 = BashOperator(
    task_id='task4',
    bash_command='echo "Hello World from Task 4"',
    dag=sub_dag)


t2.set_upstream(t1)
t3.set_upstream(t2)
t4.set_upstream(t3)