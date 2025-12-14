'''
create_conn
create_database

CRUD:
    add_new_note
    get_all_tasks
    update_note
    dalete_note
'''


import sqlite3
from classes import Task


def connect_to_db(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('tasks.sqlite')
        curs = conn.cursor()
        kwargs.update(curs=curs)

        result = func(*args,**kwargs)

        conn.commit()
        conn.close()

        return result
    return wrapper

@connect_to_db
def create_database(curs:sqlite3.Cursor):
    curs.execute(
        '''CREATE TABLE IF NOT EXISTS Tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER)''')

@connect_to_db
def add_new_note(task:Task, curs:sqlite3.Cursor):
    curs.execute(
        'INSERT INTO Tasks (title,description,completed) VALUES (?,?,?)',
        (task.title, task.description, task.completed)
        )

@connect_to_db   
def get_all_tasks(curs:sqlite3.Cursor):
        curs.execute('SELECT * FROM Tasks')
        tasks = curs.fetchall()

        tasks = [Task(*task) for task in tasks]
        return tasks

@connect_to_db
def update_note(task:Task, curs:sqlite3.Cursor):
    curs.execute(
         '''
        UPDATE Tasks
        SET title = ?, description = ?, completed = ?
        WHERE id = ?
        ''',
        (task.title, task.description, task.completed, task.pk)
    )
     
@connect_to_db
def delete_notes(task:Task, curs:sqlite3.Cursor):
    curs.execute(
         '''
        DELETE FROM Tasks
        WHERE id = ?
        ''',
        (task.pk,) # need a comma so python will know that is cortege with one element
    )
