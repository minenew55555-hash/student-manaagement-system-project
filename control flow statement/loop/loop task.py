# temperatures = [30,32,28,35,31,29,34]
# average = sum (temperatures) / len (temperatures)
# total = 0
# for temp in temperatures:
#     if temp > average:
#         total += 1
# print(total)

# usernames = ["aaliya","jyothi lekshmi","meharunissa","naziya","farhana"]
# for a in usernames:
    # if len(a) > 8:
    #    print(a)
    
# integers = [1,2,6,7,1,3,2,3,4,5,6,]
# unique = []
# for num in integers:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# integers = [1,2,6,7,1,3,2,3,4,5,6,]
# unique = set(integers)
# print(unique)

# sentence = "i like python coz python is easy and i enjoy learning python everyday"
# words = sentence.split()
# count = {}
# for i in words:
#     if i in count:
#         count[i] += 1
#     else :
#         count[i] = 1
# print(count)

# trans = [1000,-200,500,-100,300]
# balance = 0
# for money in trans:
#     balance = balance + money
# print("final balance :",balance)

# emails = ["aaliya@gamail.com","hai.com","me@com"]
# for mail in emails:
#     if "@" in mail and "." in mail:
#         print("valid")
#     else :
#         print("invalid")

# numbers = [100,200,500,750,800]
# largest = 0
# secondlarge = 0
# for i in numbers:
#     if i > largest:
#         secondlarge = largest
#         largest = i
#     elif i > secondlarge:
#         secondlarge = i
# print("secondlarge :", secondlarge)

# numbers = [[1,2],[3,4],[5]]
# flat = []
# for i in numbers:
#     for j in i:
#         flat.append(j)
# print(flat)

# for i in range(10,101,10):
#     print("loading",i,"%")

# numbers = [1,2,3,4,5]
# k = 2
# for i in range(k):
#     last = numbers.pop()
#     numbers.insert(0,last)
# print(numbers)

# users = [{"name":"ali","age":25,"active":true},{"name":"sara","age":21,"active":true},{"name":"john","age":40,"active":false}]
# print("active users:")
# for 

#nested loop

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end= " ")
#     print()

# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end= " ")
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(n - i):
#         print(" ",end= " ")
    
#     for j in range(i):       
#         print("*",end= " ")
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#        print(j,end="")
#     print()

# n = 5
# for i in range(5,0,-1):
#     for j in range(i):
#         print(j+1,end="")
#     print()

# for i in range(0,5):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()

