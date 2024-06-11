class College:
    def open(self):
        print("college open")

class Cls(College):
    def started(self):
        print("college started")
class Student(Cls):
    def close(self):
        print("closed")

obj=Student()
print(obj.open())