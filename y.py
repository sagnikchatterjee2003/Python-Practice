num = int(input("Enter any number"))
count = 0
while num > 0:
    num = num//10
    count = count + 1
print("Number of digits: %d" %count)
