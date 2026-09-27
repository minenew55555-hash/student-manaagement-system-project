# def greet():
#     print("good morning!")
# greet()

# def square():
#     a = int(input("enter a number"))
#     print(a*a)
# square()

# def cube():
#     a = int(input("enter a number"))
#     print(a*a*a)
# cube()

# def even_odd():
#     a = int(input("enter a number"))
#     if a%2==0:
#         print("even")
#     else :
#         print("odd")
# even_odd()

# def largest():
#     a = int(input("enter a number"))
#     b = int(input("enter a number"))
#     if a>b:
#         print("a is the largest")
#     else :
        # print("b is the largest")
# largest()

# def smallest():
#     a = int(input("enter a number"))
#     b = int(input("enter a number"))
#     c = int(input("enter a number"))
#     print(min(a,b,c))
# smallest()

# def smallest():
#     a = int(input("enter a number :"))
#     b = int(input("enter a number : "))
#     c = int(input("enter a number : "))
#     if a<b:
#         if a<c:
#             print(a)
#         else :
#             print(c)
#     else :
#         if b<c:
#             print(b)
#         else :
            # print(c)
# smallest()

# def table():
#     n = int(input("enter a number"))
#     for i in range(1,11):
#         print(n*i)  
# table()

# def table():
#     n = int(input("enter a number"))
#     for i in range(1,11):
#         print(n, "*", i, "=", n *i)
# table()

# def sum():
#     a = int(input("enter anumber"))
#     b = int(input("enter a number"))
#     c = a+b
#     print(c)
# sum()

# def factorial():
#     n = int(input("enter a number"))
#     fact = 1
#     for i in range (1,n+1):
#        fact = fact * i
#     print (fact)
# factorial()

# def reverse():
#     a = input("enter a number")
#     print(a[::-1])
# reverse()

# def palindrome():
#     a = (input("enter a number :"))
#     if a == a[::-1]:
#         print("palindrom")
#     else :
#         print("not palindrom")
# palindrome()

# def count():
#     a =(input("enter a number"))
#     print(len(a))
# count()

# def prime():
#     a = int(input("enter a number : "))
#     for i in range(2,a):
#         if a % i == 0:
#             print("not prime")
#             return                
#             print("prime")
# prime() 

# def natural():
#     n = int(input("enter a number"))
#     for i in range(1,n+1):
#         print(i)
# natural()

# def armstrong():
#     n = (input("enter a number :"))
    
#     if sum(int(i) ** 3 for i in n)==int(n):
#         print("armstrong")
#     else :
#         print("not armstrong")   
# armstrong()

# def vowels():
#     n = (input("enter a string : "))
#     count = 0
#     for i in n:
#         if i in "AEIOUaeiou":
#             count = count + 1
#     print("number of vowels :",count)
# vowels()

# def reverse():
#     text = input("enter a string : ")
#     print(text[::-1])
# reverse()

# def palindrome():
#     text = input("enter a string : ")
#     if text[::-1]:
#         print("palindrome")
#     else :
#         print("not palindrome")
# palindrome()

# def calculator():
#     a = float(input("enter a number : "))
#     b = float(input("enter a number : "))
#     op = input("enter operator ( +,-,*,/) :")
#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         print(a / b)
#     else :
        # print("invalid operator")
# calculator()

# def add(a,b):  
#       return a+b
# print(add(4,5))

# def add(a,b,c):
#       return a+b+c
# print(add(2,3,4))

#multiple argument
# def adder(*a):
#     result = 0
#     for i in a:
#         result+=i
#     return result
# print(adder(10,5,7))
# print(adder(10,3))
# print(adder(10,20,3,4,5,6,78,12,34,56,67))

# def reverse():
#     return a[::-1]
# a = input("enter a string: ")
# print(reverse())

# def palindrome(a):
#     return a[::-1]
# a = input("enter a number")
# print(palindrome(a))
# palindrome(a)

def pal(p):
    if p == p[::-1]:
        return True
    else :
        return False
p=input("enter the string")
print(pal(p))
