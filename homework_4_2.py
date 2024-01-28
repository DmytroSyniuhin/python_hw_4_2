list_1 = [0, 1, 7, 2, 4, 8]
count_1 = 0
total_1 = 0
if len(list_1) > 0:
    while count_1 < len(list_1):
        if count_1 % 2 == 0:
            total_1 += list_1[count_1]
        count_1 += 1
    total_1 *= list_1[-1]
print(total_1)


list_2 = [1, 3, 5]
count_2 = 0
total_2 = 0
if len(list_2) > 0:
    while count_2 < len(list_2):
        if count_2 % 2 == 0:
            total_2 += list_2[count_2]
        count_2 += 1
    total_2 *= list_2[-1]
print(total_2)


list_3 = [6]
count_3 = 0
total_3 = 0
if len(list_3) > 0:
    while count_3 < len(list_3):
        if count_3 % 2 == 0:
            total_3 += list_3[count_3]
        count_3 += 1
    total_3 *= list_3[-1]
print(total_3)


list_4 = []
count_4 = 0
total_4 = 0
if len(list_4) > 0:
    while count_4 < len(list_4):
        if count_4 % 2 == 0:
            total_4 += list_4[count_1]
        count_4 += 1
    total_4 *= list_4[-1]
print(total_4)
