class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def push_task(self, task):
        self.tasks.insert(0, task)  # Insertar al principio de la lista

    def pop_task(self):
        if self.tasks:
            return self.tasks.pop()
        return None

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def replace_task(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description

    def get_tasks(self):
        return self.tasks

class TaskManager:
    def __init__(self):
        self.users = {
            'user1': User('user1'),
            'user2': User('user2'),
            'user3': User('user3')
        }

    def assign_task(self, username, task_description):
        if username in self.users:
            task = Task(task_description)
            self.users[username].push_task(task)

    def get_user_tasks(self, username):
        if username in self.users:
            return self.users[username].get_tasks()

    def complete_task(self, username, task_index):
        if username in self.users:
            self.users[username].complete_task(task_index)

    def pop_task(self, username):
        if username in self.users:
            return self.users[username].pop_task()

    def replace_task(self, username, task_index, new_description):
        if username in self.users:
            self.users[username].replace_task(task_index, new_description)
