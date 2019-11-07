rows=int(input('rows : '))
for i in range(rows):
    print()
    num = 1
    for j in range(i+1):
        print(j, end=" ")
        num = num*(i-j)/(i+1)
    print(('%' + str((rows - i)*2) + 's') %(" "), end="") 
      
      
 output:
R:\pythonworkspace>py pattern.py
rows : 5

0
0 1
0 1 2
0 1 2 3
0 1 2 3 4 
      