import json
def remove_student():
    name = input("enter student name to remove: ")
    with open("students.json","r") as file:
        students = json.load(file)
        found = False
    for student in students:
            if student["name"].lower() == name.lower():
                students.remove(student)
                found = True
                break
    if found:
         with open("students.json","w") as file:
              json.dump(students,file,indent = 4)
              print("student removed sucesssfully")
    else :
     print("student not found")
