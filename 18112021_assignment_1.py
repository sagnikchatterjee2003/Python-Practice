NumList = [56, 86, 45, -35, -34, -21, 4]
Number = len(NumList)

for i in range(Number):
    for j in range(i + 1, Number):
        if NumList[i] > NumList[j]:
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print(f"Highest number in the list :{NumList[Number - 1]}")
