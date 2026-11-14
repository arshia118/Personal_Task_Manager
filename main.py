from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv 
import os 

load_dotenv()


name = input("enter your name: ")
print("hello", name, "welcome to your personal task manager")
admin_mod = input("do you want to enter admin mode? yes/no: ")
if admin_mod == "yes":
    password = input("enter admin password : ")
    if password == os.getenv("admin_pass"):
        print("admin mod activated")
    else:
        print("wrong password")
tasks = load_tasks()
count = int(input("how many tasks do you want to add? : "))

for i in range(count):
    task_name = input("enter a task: ")
    prioriy =  input ("enter priority(high/medium/low): ").lower()
    task = {
        "name": task_name ,
        "priority": prioriy
    }
    tasks.append(task)

show_tasks(tasks)
save_tasks(tasks)
load_tasks()
