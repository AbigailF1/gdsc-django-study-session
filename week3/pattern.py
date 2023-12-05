print("Enter the letter you want to use for the pattern")
char = input()
if len(char) != 1:
    print("invalid input")
    exit()
for i in range(1,10, 2):
    print(char * i)
