

class Project:
    def __init__(self, name,student_id):
        self.name=name
        self.student_id= student_id
        self.status = "Started"

    def show_info(self):
        print(f"Project : {self.name}")
        print(f"Student : {self.student_id}")
        print(f"Status : {self.status}")

my_work = Project("MDA Bootcamp", "123456")
my_work.show_info()