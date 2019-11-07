rows = int(input('rows : '))
for i in range(rows):
    print(('%' + str((rows - i) * 2) + 's') % (" "), end="")
    num = 1
    for j in range(i + 1):
        print('*', end=" ")
        num = num * (i - j) / (j + 1)
    print(" ")
