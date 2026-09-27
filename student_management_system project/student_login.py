import json

def student_login():
    login_email = input("Enter your email: ")
    login_password = input("Enter your password: ")

    with open("students.json","r") as file:
        students = json.load(file)

    for student in students:
        if student["email"] == login_email and student["password"] == login_password:
         print("login sucessfully")
         return True
    print("invalid email or password")
    return False
    