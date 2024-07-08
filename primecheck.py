def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
        else:
            return 1


N = int(input("Enter the Range: "))
for j in range(1, N+1):
    if j == 1:
        continue
        # print(f"{j} is not prime")
    else:
        prime = is_prime(j)
        if prime == 1:
            print(f"{j} is prime")
        else:
            continue
            # print(f"{j} is not prime")
