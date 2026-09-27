import json

def assign_class():
    name = input("enter student name: ")
    class_name = input("enter course: ")
    with open("students.json","r") as file:
        students = json.load(file)
        for student in students:
                if student["name"] == name:
                   student["class_name"] = class_name
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)
        print("class assigned sucessfully")

