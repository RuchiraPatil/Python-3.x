import sys
if len(sys.argv)==2:
    num = int(sys.argv[1])
else:
    num = int(input('Number : '))
for i in range(1,21):
    print(num, ' * ', i, ' = ', i * num)
