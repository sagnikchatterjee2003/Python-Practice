# Question 4

print("Following are the numbers divisible by 7 and are multiples of 5, in thr range of 1500 and 2700:-")
for i in range(1500, 2701):
    if i % 7 == 0:
        if i % 5 == 0:
            print(i)
