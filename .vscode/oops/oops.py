# class new:
#     x = 10
# object = new()
# print(object.x)


# constructor
# class students:
#     def __init__(self,name,tech):
#          self.name = "aaliya"
#          self.tech = "python"

# students1=students("aaliya","python")
# print(students1.name)
# print(students1.tech)

# class car:
#     def __init__(self,model,company):
#         self.model = model
#         self.company = company

# car1=car("BMW","BMW 3 series")
# car2=car("swift","hyundai")
# print(car1.model)
# print(car1.company)
# print(car2.model)
# print(car2.company)


#string method
# class students:
#     def __init__(self,name,tech,age,place):
#         self.name = name
#         self.tech = tech
#         self.age = age
#         self.place = place
#     def __str__(self):
#         return f"name:{self.name},tech:{self.tech},age:{self.age},place:{self.place}"
    
# s1 = students("aaliya","data",23,"kaduvayil")
# print(s1)


# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# student1 = student("aaliya",23)
# print(student1.name)
# print(student1.age)

#DESTRUCTOR
# class book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def __str__(self):
#         return f"title:{self.title},author:{self.author}"
#     def __del__(self):
#         return f"deleted"
# b1 = book("harry potter","rowling")
# print(b1)


#USER CREATION (DISPLAY)
# class student:
#     def __init__(self,name,tech):
#         self.name = name
#         self.tech = tech
#     def display(self):
#         return f"{self.name},{self.tech}"
# s1 = student("aaliya","data")
# print(s1.display())


# class book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def display(self):
#         return f"{self.title},{self.author}"
# b1 = book("harry potter","rowling")
# print(b1.display())


# class rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         area = self.length * self.width
#         print("area:",area)
# r1 = rectangle(10,5)
# r1.area()


# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         area = self.radius * 3.14
#         print("area:",area)
# c1 = circle(5)
# c1.area()


# class bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         updated_balance = self.balance + amount
#         print("updated_balance:",updated_balance)
# account = bankaccount(1000)
# account.deposit(500)


# class temperature:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     def fahrenheit(self):
#         celsius = float(input("enter a celsius: "))
#         fahrenheit = (celsius * 9/5)+32
#         print("fahrenheit",fahrenheit)
# temp = temperature(32)
# temp.fahrenheit()


# class temperature:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     def fahrenheit(self):
#         fahrenheit = (self.celsius * 9/5)+32
#         print("fahrenheit",fahrenheit)
# temp = temperature(32)
# temp.fahrenheit()


# class product:
#     def __init__(self,product_name,price):
#         self.product_name = product_name
#         self.price = price
#     def product_details(self):
#         print("product_name:",self.product_name)
#         print("price:",self.price)
# p1 = product("bottle",80)
# p1.product_details()


# class car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#     def display(self):
#         print("brand:",self.brand)
#         print("price:",self.price)
# car1 = car("toyota",1500000)
# car1.display()


# class triangle:
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         area = 0.5 * self.base * self.height
#         print("area:",area)
# t1 = triangle(10,5)
# t1.area()

