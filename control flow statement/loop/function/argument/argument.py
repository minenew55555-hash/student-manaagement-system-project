# def add(a=0,b=0,c=0):
#       return a+b+c
# print(add(2,3,4))              #default argument
# print(add(2,4))
# print(add(2,3,4,5,6))

# a = ["aaliya","naziya","jyothi","farhana","aswin","lekshmi","nikheta"]

def add(*a):
    result = 0
    for num in a:
        result += num            #multiple argument
    return result
print(add(1,2,3,4,5))

