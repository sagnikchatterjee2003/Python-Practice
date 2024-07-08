# Question 2

a = [7, 2, 8, 9, 15, 10, 12, 22, 11, 21, 26, 51, 14, 55, 29, 36, 57]
s = len(a)
print("Original Array")
for i in range(s):
    print(a[i])
for i in range(s):
    for j in range(i + 1, s):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Sorted Array")
for i in range(s):
    print(a[i])
