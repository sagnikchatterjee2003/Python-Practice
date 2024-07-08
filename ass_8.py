def multiplier(a):
    return lambda x: a*x


num = int(input("Enter input: "))
multi = multiplier(5)
print(multi(num))
