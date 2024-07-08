# Question 7

string = "Umbrella"
count = 0
for i in range(len(string)):
    if string[i] == 'E':
        count = count + 1
print(f"No. of 'E' in {string} is : {count}")
