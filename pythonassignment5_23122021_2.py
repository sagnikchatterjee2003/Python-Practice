# Question 2

a = "Programming and Problem Solving using Python"
b = ""
s = len(a)

while s > 0:
    b = b + a[s-1]
    s = s - 1

print(f"Original String : {a}")
print(f"Reversed String : {b}")
