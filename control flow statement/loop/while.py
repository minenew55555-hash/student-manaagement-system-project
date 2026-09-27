# a = 0
# while True:
#     b = input("enter the word")
#     if b == "exit":
#         break
#     a += 1


# while 1:
#     b = input("enter the valid integer:")
#     if b.isdigit():
#         print("valid integer:" ,b)
#         break
#     else :
#         print ("invalid integer:")


# for attempt in range(1,4):
#     pw = input("enter a password:")
#     if pw == "12345":
#         print("success:")
#         break
#     else :
#         print("unsucess:")
# else :
#     print("reached attempt:")

# a = int(input("enter a number:"))
# while a >= 0 :
#     a = a -1
#     print(a)
#     if a == 0:
#         print("time is up")
#         break

# logs = ["error 404","error 300","error 404","error 350","error 300"]
# error = {}
# for i in logs:
#     if i in error:
#        error[i] += 1
#     else :
#         error[i] = 1
# print(error)

# a = [1,2,3,4,7,8.9,11,12,13,14,15]
# count = 1
# longest = 1
# for i in range(1,16):
#     if a[i] == a[i - 1] + 1:
#         count = count + 1
#     else :
#         count = 1
#     if count>longest:
        # longest = count
# print("longest streak:",longest)

# preferences = ["pizza","kfc","noodles"]
# items = ["pizza","burger","alfam","noodles","beef","poratto"]
# recommended = []
# for item in items:
#     if item in preferences:
#         recommended.append(item)
# print(recommended)

# users = [{"name":"aaliya","age":22,"active":True},{"name":"manu","age":35,"active":False}
#          ,{"name":"ruksana","age":40,"active":True}]
# active_users = []
# older_users = []
# missing_fields =[]
# for i in users:
#    if i["active"]==True:
#             print("active users:",i["name"])
# for i in users:
#    if i["age"]>30:
#             print("older than 30:",i["name"])
# for i in users:
#       if "active" not in i:
#             print("missing fields:",i["name"])

#normal loop
# names = ["ali","sara","john"]
# for i in range(len(names)):
#     print(i,names[i])

# #enumerate():
# names = ["ali","sara","john"]
# for i,names in enumerate(names):
#     print(i,names)

#normal loop
# names = ["ali","sara","john"]
# ages = [20,25,30]
# for i in range(len(names)):
#     print(names[i],ages[i])

#  #zip():
# names = ["ali","sara","john"]
# ages = [20,25,30]
# for name,age in zip(names,ages):
#     print(name,age)

#fix an inefficient loop
# numbers = [1,2,3,4,5]
# for i in numbers:
#     for j in numbers:
#         print(i)

#better loop
# numbers = [1,2,3,4,5]
# for i in numbers:
#     print(i)
