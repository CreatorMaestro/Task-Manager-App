class Task:
    def __init__(self, pk=None, title=None, description=None, completed=False):
        self.pk = pk
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        if self.completed == True:
            status = 'done'
        else:
            status = 'not done'
        return f'{self.title}: {self.description} - {status}'
    
    def mark_done(self):
        task_state = input('Is your planned task done? (yes/no)')
        if task_state == 'yes':
            self.completed = True
            return self.completed
        else:
            return self.completed

