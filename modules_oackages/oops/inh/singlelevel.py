class College:
    def open(self):
        print("school open")
class Student(College):
    def start(self):
        print("class started")

obj=Student()
print(obj.open())
print(obj.start())


