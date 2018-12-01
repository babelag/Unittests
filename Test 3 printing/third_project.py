
class Profile:

    def __init__(self, name, age, job):
        self.job = job
        self.age = age
        self.name = name

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def print_job(self):
        print(self.job)
