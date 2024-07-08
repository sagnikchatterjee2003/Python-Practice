def even_adder(l1, l2):
    i = l1
    add = 0
    while i <= l2:
        if i % 2 == 0:
            add = add + i
        i = i + 1
    print(add)


even_adder(1, 10)
