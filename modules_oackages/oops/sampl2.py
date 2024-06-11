class School:
    def __init__(self):
        print("hi")
    x=9
    def sum(self):
        print(self.x)
class Stud(School):
    def s(self):
        print("python")

obj=Stud()
print(obj.sum())