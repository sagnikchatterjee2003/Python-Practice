def palindrome_check(num1):
    final = 0
    backup = num1
    while backup > 0:
        ld = backup % 10
        final = (final * 10) + ld
        backup = backup // 10
    if num1 == final:
        print(f"{num1} is a palindrome number")
    else:
        print(f"{num1} is not a palindrome number")


a = int(input("Enter the number :"))
palindrome_check(a)
