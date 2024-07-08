# Question 1

a = [1, 2, 8, 2, 3, 8, 2, 2, 1, 2, 2, 5, 1, 5, 2, 3, 5]
s = len(a)
for i in range(s):
    w = a[i]
    if w != 0:
        f = 0
        for j in range(s):
            if a[j] == w:
                f += 1
            else:
                continue
        print(f"Frequency of {w} = {f}")
        for k in range(s):
            if a[k] == w:
                a[k] = 0
