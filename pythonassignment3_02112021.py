# Question 3

def swapper(num1, num2):
    print(f"Original numbers: Number1 = {num1} , Number2 = {num2}")
    temp = num1
    num1 = num2
    num2 = temp
    print(f"Original numbers: Number1 = {num1} , Number2 = {num2}")


a = int(input("Number1 = "))
b = int(input("Number2 = "))
swapper(a, b)
