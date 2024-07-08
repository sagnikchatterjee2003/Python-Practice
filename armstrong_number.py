num = int(input("Enter the number to be checked: "))
# number taken from user
dup = num
# taking a duplicate variable to store the original number
s = 0

# loop to calculate the sum of cubes of every digit of the original number
while dup != 0:
    r = dup % 10
    s = s + (r**3)
    dup = dup//10

# checking if the sum is equal to the original number
if s == num:
    print(f"{num} is Armstrong Number.")
else:
    print(f"{num} is not Armstrong Number.")
