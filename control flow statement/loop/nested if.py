# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))
# if a > b:
#     if a > c:
#         print("a is the largest")
#     else :
#         print("c is the largest")
# else :
#     if b > c:
#         print("b is the largest")
#     else :
#         print("c is the largest")

# a = int(input("enter a number"))
# if a >= 0:
#     if a == 0:
#         print("a is zero")
#     else :
#         print("a is positive")
# else :
#          print("a is negative")


# marks = int(input("enter a number"))
# if marks >= 40:
#     if marks >= 75:
#         print("distinction")
#     else :
#         print("passed")
# else :
#     print("failed")


# age = int(input("enter a number"))
# salary = int(input("enter a number"))
# if age >= 21:
#     if salary >= 25000:
#         print("eligible")
#     else :
#         print("not eligible")
# else :
#     print("not eligible")


# units = int(input("enter a number"))
# if units <= 100:
#     bill = units * 2
# else :
#     if units <= 200:
#         bill = units * 3
#     else :
#         bill = units * 5
# print("electricity bill = ",bill)


# yr = int(input("enter a number"))
# if yr % 4 == 0:
#     if yr % 100 == 0:
#         if yr % 400 == 0:
#             print("leap year")
#         else :
#             print("not a leap year")
#     else :
#         print("leap year")
# else :
#     print("not a leap year")


# number = int(input("enter a number"))
# if number % 3 == 0:
#     if number % 5 == 0:
#         print("number is divisible by 5 and 3")
#     else : 
#         print("number is divisible only by 3")
# else :
#     if number % 5 == 0:
#         print("divisble only by 5")
#     else :
#         print("not divisible by 5 and 3")


# experience = int(input("enter a number"))
# salary = int(input("enter a number"))
# if experience > 5:
#     if salary > 50000 :
#         bonus = salary * 10 / 100
#         print("the bonus:",bonus)
#     else :
#         bonus = salary * 5 / 100
#         print("the bonus:",bonus)
# else :
#     print("not eligible")


# username = input("enter username:")
# password = input("enter username:")
# if username == "aaliya":
#     if password == "12345":
#         print("login succesfully")
#     else :
#         print("wrong pw")
# else :
#     print("wrong username")


a = int(input("enter a side 1 :"))
b = int(input("enter a side 2 :"))
c = int(input("enter a side 3 :"))
if a == b:
    if b == c:
        print("equilateral triangle")
    else :
        print("isosceles triangle")
else :
    if b == c:
        print("isosceles triangle")
    else :
        if a == c:
            print("isosceles triangle")
        else :
            print("scalene triangle")