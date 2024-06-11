class College:
    def open(self):
        print("college open")

class Cls:
    def started(self):
        print("college started")
class Student(College,Cls):
    def close(self):
        print("closed")

obj=Student()
print(obj.started())