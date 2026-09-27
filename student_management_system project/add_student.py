
import json

def add_student():
    name = input("enter student name: ")
    age = input("enter student age: ")
    email = input("enter student email: ")
    password = input("enter student password: ")
    student = {"name":name,
               "age" :age,
               "email" :email,
               "password" :password,
               "class_name" :""}
    
    with open("students.json","r") as file:
        students = json.load(file)
    students.append(student)
    with open("students.json","w") as file:
        json.dump(students,file,indent = 4)
    print("student added successfully")



