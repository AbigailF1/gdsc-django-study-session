summ = 0
fiveandthree = 0
for i in range(2, 51, 2):
    if i % 3 == 0 and i % 5 == 0:
        print("FiveandThree")
    elif i % 3 == 0:
        print("Three")
        fiveandthree += 1
    elif i % 5 == 0:
        print("Five")
        fiveandthree += 1
    else:
        print(i)
    summ += i
