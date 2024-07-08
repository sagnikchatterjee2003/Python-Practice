Word = input("Enter the string to be checked : ")
s = len(Word)
Word = Word.upper()
dup = s
a = 0
flag = 1

while dup > 0:
    dup = dup - 1
    w = Word[a]
    for i in range(s):
        if a != i:
            if w == Word[i]:
                flag = 0
                break
            else:
                continue
        else:
            continue
    a = a + 1

if flag == 1:
    print(f"{Word} is an Unique String.")
else:
    print(f"{Word} is not an Unique String.")
