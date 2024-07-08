def num_reversal(num1):
    final = 0
    backup = num1
    while backup > 0:
        ld = backup % 10
        final = (final * 10) + ld
        backup = backup // 10
    print(f"Reverse of {num1} is {final}")


a = int(input("Enter the number :"))
num_reversal(a)
