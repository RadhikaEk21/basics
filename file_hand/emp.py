def emp_details(no):
    with open("emp.txt",'w') as f:
        for i in range(1,no+1):
            print(f"Enter the details of {i} ")
            name=input("Enter your name  ")
            Id=int(input("Enter your id "))
            position=input("Enter your designation ")
            f.write(f"employee {i} details \n")
            f.write(f"Name : {name}\n")
            f.write(f"Id Number : {id}\n")
            f.write(f"Designation : {position}\n")
            f.write(f"\n")


num=int(input("enter the limit"))
emp_details(num)
