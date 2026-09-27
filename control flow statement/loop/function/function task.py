# def reverse(a):
#     return a[::-1]
# a = (input("enter a string"))
# print(reverse(a))

# def palindrome(p):
#     return p == p[::-1]
# p = input("enter a string")
# print(palindrome(p))

# def vowels(v):
#     count = 0
#     for char in v:
#         if char in "aeiouAEIOU":
#             count += 1
#     return count
# v = input("enter a string")
# print(vowels(v)) 

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a)
#         a,b = b,a+b
# n = int(input("enter number of terms: "))
# fibonacci(n)

# def sumlist(numbers):
#     total = 0
#     for i in numbers:
#        total += i
#     return total
# numbers = [1,23,3,4,5,6,7]
# print(sumlist(numbers))

# def maximum(a):
#     return max(a)
# a = [1,23,4,5,6,7,8,9]
# print(maximum(a))
# maximum(a)

# def remove(a):
#     result = []
#     for num in a:
#         if num not in result:
#             result.append(num)
#     return result
# a = [1,2,3,4,5,6,7,8,2,3,4,5]
# print(remove(a))

# def sort(a):
#     for i in range(len(a)):
#         for j in range(i + 1,len(a)):
#             if a[i]>a[j]:
#                 temp = a[i]
#                 a[i] = a[j]
#                 a[j] = temp
#     return a
# a = [5,2,4,1,3]
# print(sort(a))

# def sort(a):
#     a.sort()
#     return a
# a = [5,4,1,2,3]
# print(sort(a))

# def frequency(a):
#     result = {}
#     for num in a:
#         if num in result:
#             result[num] = result[num]+1
#         else :
#             result[num] = 1
#     return result
# a = [1,2,2,3,3,3,4]
# print(frequency(a))

# def anagram(str1,str2):
#     if sorted(str1) == sorted(str2):
#         return True
#     else :
#         return False
# str1 = "listen"
# str2 = "silent"
# print(anagram(str1,str2)) 

# def anagram(str1,str2):
#     if sorted(str1) == sorted(str2):
#         return True
#     else :
#         return False
# str1 = "aaliya"
# str2 = "naziya"
# print(anagram(str1,str2))

