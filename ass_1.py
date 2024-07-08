a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))
c = int(input("Enter the 3rd number :"))

if a > b and a > c:
    print(f"Highest number = {a}")
elif b > a and b > c:
    print(f"Highest number = {b}")
elif c > a and c > b:
    print(f"Highest number = {c}")
