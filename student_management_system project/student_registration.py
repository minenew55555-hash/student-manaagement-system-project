import json
def register_student(): 
    name = input("enter your name: ")
    age = input("enter your age: ")
    email = input("enter your email: ")
    password = input("enter your password: ")
    student = {"name":name,"age":age,"email":email,"password":password}
    with open ("student_management_system project/students.json","r") as file:
        students = json.load(file)
        students.append(student)
        for student in students:
            print("name:",student["name"])
            print("age:",student["age"])
    with open("student_management_system project/students.json","w") as file:
        json.dump(students,file,indent=4)
        print("registration successfully")







