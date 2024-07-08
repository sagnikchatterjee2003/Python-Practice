def odd_printer(l1, l2):
    while l1 <= l2:
        if l1 % 2 != 0:
            print(l1)
        l1 = l1 + 1


print("Odd numbers :")
odd_printer(50, 100)
