import json
def search_student():
    name = input("enter student name: ")
    with open("students.json","r") as file:
        students = json.load(file)
    for student in students:
        if student["name"].lower() == name.lower():
            print("student found !")
            print("name:",student["name"])
            print("age:",student["age"])
            print("email:",student["email"])
            print("class:",student.get("class_name"))
            return
    print("student not found")
