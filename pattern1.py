rows=int(input('rows : '))
for i in range(rows):
    print()
    num = 1
    for j in range(i+1):
        print(i, end=" ")
        num = num*(i-j)/(i+1)
    print(('%' + str((rows - i)*2) + 's') %(" "), end="") 
      
      
      output:
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6 6 6