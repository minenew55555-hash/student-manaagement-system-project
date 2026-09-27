import json
def raise_doubt():
    name = input("enter student name: ")
    doubt = input("enter your doubt: ")
    try:
        with open("doubts.json","r") as file:
            doubts = json.load(file)
    except FileNotFoundError:
        doubts = []
        new_doubt = {"student_name":name,"doubt":doubt}
        doubts.append(new_doubt)
        with open("doubts.json","w") as file:
            json.dump(doubts,file,indent = 4)
            print("doubt submitted successfully")

