import datetime
import database as db
from classes import Task
import os
from middlewares import console_clear

class TaskManager:
    def __init__(self):
        self.task_list: list[Task] = db.get_all_tasks()
    
    def console_interaction(self):
        console_choice = ''
        while console_choice != '5':
            print('-'*50)
            print('Welcome to task manager, helps you everyday to be better version of you')
            print('What do you want to do today sir?')
            print('1. Add task\n2. Show all tasks\n3. Mark the task completed\n4. Delete task\n5. Quit')
            console_choice = input('Which action do you want?')

            if console_choice == '1':
                self.add_task()
            elif console_choice == '2':
                self.show_tasks()
            elif console_choice == '3':
                self.mark_task_done()
            elif console_choice == '4':
                self.delete_task()
            elif console_choice == '5':
                print('Bye now, waiting for your return')
            else:
                print('Picked wrong choice')

    @console_clear
    def add_task(self):
        additional_task_title = input('Write your new task: (title)')
        additional_task_description = input('Write your new task: (description)')
        
        if self.task_list:
            last_task_pk = self.task_list[-1].pk
            current_pk = last_task_pk + 1
        else:
            current_pk = 1
            current_pk += 1
        additional_task = Task(current_pk, additional_task_title, additional_task_description)
        self.task_list.append(additional_task)
        db.add_new_note(additional_task)

    @console_clear
    def show_tasks(self):
        date_time = datetime.datetime.now()
        print(date_time)
        for i, task in enumerate(self.task_list, start=1):
            print(f'{i}. {task}')
        
    def show_tasks_noclear(self):
        date_time = datetime.datetime.now()
        print(date_time)
        for i, task in enumerate(self.task_list, start=1):
            print(f'{i}. {task}')
        
    @console_clear
    def mark_task_done(self):
        self.show_tasks_noclear()
        completed_task = int(input('Which task do you want to mark? (number)'))
        index = completed_task - 1
        if index < 0 or index >= len(self.task_list):
            print('Your input has wrong index, check it!')
            return
        else:
            task = self.task_list[index]
            task.completed = not task.completed
            self.show_tasks_noclear()
            db.update_note(task)

    @console_clear
    def delete_task(self):
        self.show_tasks_noclear()
        delete_task = int(input('Which task do you want to delete? (number)'))
        index = delete_task - 1
        if index < 0 or index >= len(self.task_list):
            print('Your input has wrong index, check it!')
            return
        else:
            task = self.task_list.pop(index)
            db.delete_notes(task)


os.system('cls')
db.create_database()
t = TaskManager()


t.console_interaction()