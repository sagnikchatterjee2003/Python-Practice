N = int(input("Enter the range: "))
s = 0
for i in range(1, N+1):
    for j in range(2, i):
        if i % j == 0:
            s = 1
            break
        else:
            s = 0
    if s == 0:
        print(f"{i} prime")
    else:
        print(f"{i} not prime")
