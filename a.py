matrix = []
row = int(input("Enter the number of rows of the list: "))
column = int(input("Enter the number of columns of the list: "))
print("Enter the data rowwise: ")
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)

print(matrix)
for i in range(row):
    for j in range(column):
        print(matrix[i][j])
