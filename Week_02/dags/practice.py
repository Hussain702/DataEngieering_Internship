from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.decorators import dag
from airflow.operators.email import EmailOperator
@dag(
    start_date=datetime.today(),
    schedule="@daily",
    catchup=False,
)

def practice():

    task1=BashOperator(
        task_id='First_task',
        bash_command='echo this is first task'
    )
    task2=BashOperator(
        task_id='second_task',
        bash_command='echo this is 2nd task'
    )
    task3=BashOperator(
        task_id='third_task',
        bash_command='echo this is 3rd task'
    )
    task4=EmailOperator(
        task_id='sending_mail',
        to='mianhussain702@gmail.com',
        subject='Airflow Task Complete',
        html_content='<h3>The task has finished successfully!</h3>',
       
    )
    task1>>task2>>task3>>task4
   # task1.set_downstream(task2)
practice()    