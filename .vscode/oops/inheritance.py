# # class hod:
# #     def __init__(self,hname,department):
# #         self.hname = hname
# #         self.department = department

# #     def __str__(self):
# #        return f"{self.name},{self.department}"

# # class teacher(hod):
# #     def __init__(self,name,subject,hname,department):
# #         super().__init__(hname,department)
# #         self.name = name
# #         self.subject = subject

# #     def __str__(self):
# #         super().__str__()
# #         return f"teacher:{self.name},{self.subject}"
    

# # t1 = teacher("anu","python","rahul","cse")
# # print(t1)
# # print(t1.hname)
# # print(t1.department)


# # class teacher:
# #     def __init__(self,tname,subject):
# #         self.tname = tname
# #         self.subject = subject

# #     def display(self):
# #         print("tname:",self.tname)
# #         print("subject",self.subject)

# # class student(teacher):
# #     def __init__(self,name,course,tname,subject):
# #         super().__init__(tname,subject)
# #         self.name = name
# #         self.course = course

# # t1 = student("kiran","python full stack","aaliya","data analytics ")
# # print("teacher name:",t1.tname)
# # print("subject:",t1.subject)
# # print("name:",t1.name)
# # print("course:",t1.course)
 

# # MULTILEVEL INHERITANCE
# # class ceo:
# #     def __init__(self,name,company):
# #         self.name = name
# #         self.company = company

# #     def display(self):
# #         print("name",self.name)
# #         print("company",self.company)

# # class mentor(ceo):
# #     def __init__(self,mname,subject,name,company):
# #         super().__init__(name,company)
# #         self.mname = mname
# #         self.subject = subject

# #     def mdisplay(self):
# #         print("mname",self.mname)
# #         print("subject",self.subject)

# # class student(mentor):
# #     def __init__(self,sname,course,mname,subject,name,company):
# #         super().__init__(mname,subject,name,company)
# #         self.sname = sname
# #         self.course = course

# #     def sdisplay(self):
# #         print("sname",self.sname)
# #         print("course",self.course)

# # s1 = student("aaliya","data analyst","kiran","python","sangeeth","stackup")
# # s1.sdisplay()
# # s1.mdisplay()
# # s1.display()


# # class person:
# #     def __init__(self,name):
# #         self.name = name

# # class employee(person):
# #     def __init__(self,name,employee_id):
# #         super().__init__(name)
# #         self.employee_id = employee_id

# # class manager(employee):
# #     def __init__(self,name,employee_id,department):
# #         super().__init__(name,employee_id)
# #         self.department = department

# #     def display(self):
# #         print("name",self.name)
# #         print("employee_id",self.employee_id)
# #         print("department",self.department)

# # m1 = manager("aaliya",101,"data analytics")
# # m1.display()


# # class animal:
# #     def eat(self):
# #         print("animal is eating")

# # class dog(animal):
# #     def bark(self):
# #         print("dog is barking")

# # class puppy(dog):
# #     def weep(self):
# #         print("puppy is weeping")

# # p1 = puppy()
# # p1.eat()
# # p1.bark()
# # p1.weep()

# # class vehicle:
# #     def start(self):
# #         print("vehicle is starting")

# # class car(vehicle):
# #     def drive(self):
# #         print("vehicle start driving")

# # class electriccar(car):
# #     def electriccar(self):
# #         print("electric car")

# # c1 = electriccar()
# # c1.start()
# # c1.drive()
# # c1.electriccar()


# # class account:
# #     def deposit(self,amount):
# #         print("deposited:",amount)

# #     def withdraw(self,amount):
# #         print("withdraw:",amount)

# # class savingsaccount(account):
# #     def addinterest(self):
# #         print("interest added")

# # class premiumaccount(savingsaccount):
# #     pass

# # p = premiumaccount()
# # p.deposit(5000)
# # p.withdraw(1000)
# # p.addinterest()


# # class college:
# #     def __init__(self,college_name):
# #         self.college_name = college_name

# # class department(college):
# #     def __init__(self,college_name,department_name):
# #         super().__init__(college_name)
# #         self.department_name = department_name

# # class student(department):
# #     def __init__(self,college_name,department_name,student_name):
# #         super().__init__(college_name,department_name)
# #         self.student_name = student_name

# #     def display(self):
# #         print("college name:",self.college_name)
# #         print("department:",self.department_name)
# #         print("student name:",self.student_name)

# # s = student("abc college","cse","aaliya")
# # s.display()

# # class book:
# #     def __init__(self,title):
# #         self.title = title

# #     def showbook(self):
# #         print("book title:",self.title)

# # class referencebook(book):
# #     def __init__(self,title,subject):
# #         super().__init__(title)
# #         self.subject = subject

# #     def showreference(self):
# #         print("subject:",self.subject)

# # class digitalreferencebook(referencebook):
# #     def __init__(self,title,subject,format):
# #         super().__init__(title,subject)
# #         self.format = format

# #     def showdigital(self):
# #         print("format:",self.format)

# # b = digitalreferencebook("python basics","cse","pdf")
# # b.showbook()
# # b.showreference()
# # b.showdigital()


# # class employee():
# #     def __init__(self,name):
# #         self.name = name

# #     def showemployee(self):
# #         print("employee name:",self.name)

# # class developer(employee):
# #     def __init__(self,name,language):
# #         super().__init__(name)
# #         self.language = language

# #     def showdeveloper(self):
# #         print("programming language:",self.language)

# # class seniordeveloper(developer):
# #     def __init__(self,name,language,experience):
# #         super().__init__(name,language)
# #         self.experience = experience

# #     def showseniordeveloper(self):
# #         print("experience:",self.experience)

# # s = seniordeveloper("aaliya","python","5 years")
# # s.showemployee()
# # s.showdeveloper()
# # s.showseniordeveloper()


# # class university:
# #     def __init__(self,university_name):
# #         self.university_name = university_name

# # class department(university):
# #     def __init__(self,university_name,department):
# #         super().__init__(university_name)
# #         self.department = department

# # class professor(department):
# #     def __init__(self,university_name,department,professor_name):
# #         super().__init__(university_name,department)
# #         self.professor_name = professor_name

# #     def display(self):
# #         print("university name:",self.university_name)
# #         print("department:",self.department)
# #         print("professor name:",self.professor_name)

# # p = professor("ktu","cs","john")
# # p.display()


# # class mobile:
# #     def call(self):
# #         print("making a call")

# # class androidphone(mobile):
# #     def installapp(self):
# #         print("installing in app")

# # class samsungphone(androidphone):
# #     def samsungpay(self):
# #         print("using samsung pay")

# # a = samsungphone()
# # a.call()
# # a.installapp()
# # a.samsungpay()


# # class employee:
# #     def __init__(self,basic_salary):
# #         self.basic_salary = basic_salary

# #     def calculatehra(self):
# #         return self.basic_salary * 20 / 100

# # class manager(employee):
# #     def calculateda(self):
# #         return self.basic_salary * 10 / 100

# # class seniormanager(manager):
# #     def calculatebonus(self):
# #         return self.basic_salary * 5 / 100

# #     def display(self):
# #         hra = self.calculatehra()
# #         da = self.calculateda()
# #         bonus = self.calculateda()
# #         net_salary = self.basic_salary + hra + da + bonus

# #         print("basic salary:",self.basic_salary)
# #         print("hra:",hra)
# #         print("da:",da)
# #         print("bonus:",bonus)
# #         print("net salary:",net_salary)

# # salary = float(input("enter basic salary:"))
# # s = seniormanager(salary)
# # s.display()


# class student:
#     def __init__(self,mark1,mark2,mark3):
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3

#     def total(self):
#         return self.mark1 + self.mark2 + self.mark3

# class ugstudent(student):
#     def average(self):
#         return self.total()/3 

# class pgstudent(ugstudent):
#     def grade(self):
#         avg = self.average()

#         if avg >= 90:
#             return "a"
#         elif avg >= 75:
#             return "b"
#         elif avg >= 60:
#             return "c"
#         else :
#             return "fail"

#     def display(self):
#         print("total:",self.total())
#         print("average:",self.average())
#         print("grade:",self.grade())

# m1 = float(input("enter mark 1:"))
# m2 = float(input("enter mark 2:"))
# m3 = float(input("enter mark 3:"))

# s = pgstudent(m1,m2,m3)
# s.display()


# class vehicle:
#     def get_days(self):
#         self.days = int(input("enter number of days:"))

# class car(vehicle):
#     def calculate_car_rent(self):
#         return self.days * 1000

# class luxurycar(car):
#     def calculate_rent(self):
#         return self.days * 3000

# obj = luxurycar()
# obj.get_days()
# rental = obj.calculate_rent()
# print("rental amount:",rental)



#MULTIPLE INHERITANCE

# class ceo:
#     def __init__(self,name,company):
#         self.name = name
#         self.company = company


# class mentor:
#     def __init__(self,mname,subject):
#         self.mname = mname
#         self.subject = subject

# class student(ceo,mentor):
#     def __init__(self,sname,course,mname,subject,name,company):
#         ceo.__init__(self,name,company)
#         mentor.__init__(self,mname,subject)
#         self.sname = sname
#         self.course = course

#     def display(self):
#         return f'{self.sname}:{self.subject}-{self.mname}:{self.name}:{self.company}:{self.course}'

# c1 = student("sangeeth","stackup","kiran","python","aaliya","data analytics")
# print(c1.display())



# class A:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         return("making a self")

# class B:
#     def __init__(self,age):
#         self.age = age

#     def show(self):
#         return("making another self")

# class C(B,A):
#     def __init__(self,name,age,work):
#         A.__init__(self,name)
#         B.__init__(self,age)
#         self.work = work

#     def display(self):
#         return f'{self.name},{self.age},{self.work}'

# c1 = C("aaliya",22,"analyst")
# print(c1.show())


# MULTIPLE INHERITANCE

class camera:
    def takephoto(self):
        print("taking a photo")

class musicplayer:
    def playmusic(self):
        print("playing music")

class smartphone(camera,musicplayer):
    pass  











