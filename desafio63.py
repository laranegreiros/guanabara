n = int(input('quantos termos da sequencia de fibonacci vc quer? '))
t1 = 0
t2 = 1
print('{} {}'.format(t1,t2,), end='')
cont = 3
while cont<= n:
    t3 = t1 + t2
    print(' {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('fim')