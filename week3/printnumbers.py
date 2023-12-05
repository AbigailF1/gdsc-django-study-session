# print(', '.join("{:02d}".format(i) for i in range(100)))
for i in range(100):
    print("0" + str(i) if i < 10 else str(i), end=", " if i < 99 else "\n")

