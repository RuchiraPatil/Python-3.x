n1=int(input('Number #1 : '))
n2=int(input('Number #2 : '))

n1 = n1 ^ n2
n2 = n1 ^ n2
n1 = n1 ^ n2

print('n1 = ',n1, 'n2 = ',n2)
