a = [1, 5, 4, 7, 9, 3]
s = len(a)
print(f"Unsorted list: {a}")

for i in range(s):
    for j in range(i+1, s):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        else:
            continue

print(f"Sorted list: {a}")
