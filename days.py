import math


# defining a function to round numbers to the nearest lesser integer
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


# taking the 1st day of the year from the user
day_1 = input("Enter the 1st day of the year: ")
day_1 = day_1.upper()
# taking the number of day the user want to see
day_num = int(input("Give a day number from the range 2 to 365: "))
# checking whether the input by the user within the range
if day_num >= 2 and day_num <= 365:
    # defining a list containing all the 7 days of a week
    day_week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    # calculating the number of complete weeks in the number of days given by the user
    week_num = int(round_down(day_num//7))
    # calculating the number of single days after the complete weeks are removed
    days_remaining = day_num % 7
    flag = -1
    # checking that the 1st day of the year is which number of day of the week
    for i in range(7):
        if day_1 == day_week[i]:
            flag = i
        else:
            continue
    # calculating which day of the week will be the (day_num)th day of the year
    flag = flag - 1
    flag = flag + days_remaining
    if flag >= 7:
        flag = flag - 6 - 1
        # printing the final result
        print(f"The {day_num}th day of the year will be {day_week[flag]}.")
    else:
        # printing the final result
        print(f"The {day_num}th day of the year will be {day_week[flag]}.")
else:
    print("Wrong Input!!")
