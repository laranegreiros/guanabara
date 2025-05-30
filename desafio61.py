term1 = int(input('digite o primeiro termo do PA: '))
raz = int(input('digite a razão: '))
term = term1
cont = 1
while cont != 11:
    print('{}'.format(term),end='-')
    term = term + raz
    cont = cont + 1
print('fim') 
