import json
def view_students():
    with open ("students.json","r") as file:
        students = json.load(file)
        if not students:
            print("no students found")
            return
        for student in students:
            print("--------------------")
            print("name:",student.get("name",""))
            print("age:",student.get("age",""))
            print("email:",student.get("email",""))
            print("class:",student.get("class_name",""))
print("---------------------")
