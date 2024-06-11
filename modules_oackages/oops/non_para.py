class Student:
    def __init__(self,name):
        self.name1=name
    def open(self):
        print("Hi",self.name1)

# s=input("name")
obj=Student("Ammu")
obj.name1="Achu"
print(obj.open())
obj1=Student("Radhika")
print(obj1.open())