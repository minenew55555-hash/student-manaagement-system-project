def teacher_login():
    teacher_email = "teacher@gmail.com"
    teacher_password = "1234"
    login_email = input("enter teacher email: ")
    login_password = input("enter teacher password: ")
    if login_email == teacher_email and login_password == teacher_password:
        print("teacher login successfully")
        return True
    else :
        print("invalid email or password")
        return False
