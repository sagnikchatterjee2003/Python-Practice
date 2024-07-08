# Question 3

string = "Welcome to the major world of Python"
char = "m"
count = 0

for i in range(len(string)):
    if string[i] == char:
        count = count + 1

print(f"The frequency of the {char} in the string is: {count}")
