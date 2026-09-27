# def fact(n):
#     if n == 0:
#         return 1
#     else :
#         return n * fact(n-1)
# print(fact(5))


# def numbers(n):
#     if n == 0:
#         return 0
#     else :
#         return n + numbers(n-1)
# print(numbers(5))

# def numbers(n):
#     if n == 0:
#         return 
#     else :
#         numbers(n-1)
#         print(n)
# numbers(10)

# def numbers(n):
#     if n == 0:
#         return
#     else :
#         print(n)
#         numbers(n-1)
# numbers(10)

# def product(a,b):
#     if b == 0:
#         return 0
#     else :
#         return a + product(a,b-1)
# print(product(2,3))

# def power(a,b):
#     if b == 0:
#         return 1
#     else :
#         return a * power(a,b-1)
# print(power(2,5))

# def even(n):
#     if n == 0:
#         return 0
#     else :
#         if n % 2 == 0:
#            return n + even(n-1)
#         else :
#             return even(n-1)
# print(even(5))

# def odd(n):
#     if n == 0:
#         return 0
#     else :
#         if n%2 == 0:
#             return odd(n-1)
#         else :
#             return n + odd(n-1)
# print(odd(7))

# def count(n):
#     if n==0:
#         return 0
#     else :
#         return 1 + count(n//10)             # n//10 removes the last digit
# print(count(123456789))

# def digit(n):
#     if n==0:
#         return 0
#     else :
#         return n % 10 + digit(n//10)            # n%10 gets the last digit
# print(digit(123))


# INTERMEDIATE LEVEL

# def reverse(n,rev = 0):
#     if n == 0:
#         return rev
#     else :
#         return reverse(n//10 , rev * 10 + n % 10)          #rev*10 moves the existing
# print(reverse(123))                                          #number one place left


# def palindrome(n,rev = 0):
#     if n == 0:
#         return rev
#     else :
#         return palindrome(n//10,rev * 10 + n%10)
# n = 145
# if n == palindrome(n):
#     print("palindrome")
# else :
#     print("not palindrome")
# print(palindrome(n))


# def palindrome(word):
#     if len(word) <= 1:
#         return True
#     elif word[0] != word[-1]:
#         return False
#     else :
#         return palindrome(word[1:-1])
# word = "malayalam"
# print(palindrome("malayalam"))
# print(word)


# def palindrome(word):
#     if len(word) <= 1:
#         return True
#     elif word[0] != word[-1]:
#         return False
#     else :
#          return palindrome(word[1:-1])
# word = "apple"
# print(palindrome("apple"))


