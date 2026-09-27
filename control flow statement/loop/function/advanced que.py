# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return n * factorial(n-1)
# factorial(5)

# def power(x,n):
#     if n == 0:
#         return 1
#     else :
#         return x * power(x,n-1)
# print(power(2,5))


# def sum(n):
#     if n == 0:
#         return 0
#     else :
#         return n + sum(n-1)
# print(sum(5))

# def numbers(n):
#     if n > 0:
#         numbers(n-1)
#         print(n)
# numbers(5)

# def numbers(n):
#     if n>0:
#         print(n)
#         numbers(n-1)
# numbers(5)


# def product(a,b):
#     if b == 0:
#         return 0
#     else :
#         return a + product(a,b-1)
# a = int(input("enter a:"))
# b = int(input("enter b:"))
# print(product(a,b))
# product(a,b)


# def power(a,b):
#     if b == 0:
#         return 1
#     else :
#         return a * power(a,b-1)
# print(power(3,4))


# def even(n):
#     if n == 0:
#         return 0
#     elif n%2 == 0:
#         return n + even(n-1)
#     else :
#         return even(n-1)
# print(even(10))


# def odd(n):
#     if n == 0:
#         return 0
#     elif n%2 == 1:
#         return n + odd(n-1)
#     else :
#         return odd(n-1)
# print(odd(10))


# def digits(n):
#     if n == 0:
#         return 0
#     else :
#         return 1 + digits(n // 10)   #integer division so its remove last digit at each time
# print(digits(34567))


# def digisum(n):
#     if n == 0:
#         return 0
#     else :
#         return n % 10 + digisum(n//10)
# print(digisum(10))


# def digisum(n):
#     if n == 0:
#         return 0
#     else :
#         return n % 10 + digisum(n//10)       # n%10 = gets the last digit
# print(digisum(1233445))                      # n//10 = removes the last digit


def reverse(n):
    if n == 0:
        return 0
    else :
        return 