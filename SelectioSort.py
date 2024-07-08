a = []
s = int(input("Enter the size of the list: "))

print("Enter the data: ")
for i in range(s):
    x = int(input())
    a.append(x)

data = int(input("Enter the data to be searched: "))
flag = 0

for i in range(s):
    if data == a[i]:
        print("Data Found")
        flag = 1
        break

if flag == 0:
    print("Data Not Found")
