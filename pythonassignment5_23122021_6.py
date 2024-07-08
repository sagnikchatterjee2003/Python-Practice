# Question 6

string = input("Enter the string : ")
s = len(string)
for i in range(s):
    if string[i] != " ":
        print(string[i])
