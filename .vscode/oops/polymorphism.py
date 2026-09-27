# same set of code in diff situations
# method overloading
# method ovrerriding
# operator overloading
# duck typing

# method overloading: same method name with different parameters
# same method name il python work cheyyilla. python il method overloading illa. 
# but we can achieve method overloading by using default arguments.


# method overriding
# class a:
#     def add(self,name):
#         self.name = name
#         return "hello" + name

# class b:
#     def add(self,age):
#         self.age = age
#         return "your age is" + str(age)

# obj = a()
# obj1 = b()
# print(obj.add("aaliya"))
# print(obj1.add)


# class a:
#     def show(self):
#         print("show a")

# class b:
#     def show(self):
#         print("show b")

# class c:
#     def show(self):
#         print("show c")


# operator overloading

# class a:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __add__(self,other):
#         return a(self.x + other.x,self.y+other.y)

#     def __str__(self):
#         return f'({self.x},{self.y})'

# obj = a(5,2)
# obj1 = a(7,4)
# print(obj + obj1)


#duck typing
# class duck:
#     def sound (self):
#         return "quack quack"

# class dog:
#     def sound (self):
#         return "bark bark"

# class cat:
#     def sound (self):
#         return "meow meow"

# def make_sound(animal):
#      return animal.sound()

# duck1 = duck()
# dog1 = dog()
# cat1 = cat()
# print(make_sound(duck1))
# print(make_sound(dog1))
# print(make_sound(cat1))






    
