from student_login import student_login

from student_registration import register_student

from teacher_login import teacher_login

from add_student import add_student

from assign_class import assign_class

from search_student import search_student

from raise_doubt import raise_doubt

from remove_student import remove_student

from view_students import view_students

def student_menu():
    while True:
        print("\n===== STUDENT MENU =====")
        print("1. raise a doubt")
        print("2. assign class")
        print("3. logout")
        choice = input("enter your choice: ")
        if choice == "1":
            raise_doubt()
        elif choice == "2":
            assign_class()
        elif choice == "3":
            print("logged out successfully")
            break
        else :
            print("invalid choice.please try again")

def teacher_menu():
    while True:
        print("\n===== TEACHER MENU =====")
        print("1. add student")
        print("2. search student")
        print("3. remove student")
        print("4. view students")
        print("5. logout")
        choice = input("enter your choice: ")
        if choice == "1": 
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("logged out sucessfully.")
            break
        else :
            print("invalid choice.please try again")

def main():
    while True:
        print("\n========================")
        print("  STUDENT MANAGEMENT SYSTEM")
        print("==========================")
        print("1. student login ")
        print("2. student register ")
        print("3. teacher login ")
        print("4. exit ")

        choice = input("enter your choice: ")
        if choice == "1":
            login_success = student_login()
            if login_success:student_menu()
        elif choice == "2":
            register_student()
        elif choice == "3":
            login_success = teacher_login()
            if login_success:teacher_menu()
        elif choice == "4":
             print("thank you!")
             break
        else :
            print("invalid choice.please try again")

if __name__ == "__main__":
    main()