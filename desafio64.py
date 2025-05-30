cont = 0
num = 0
soma = 0
while num != 999:
    num = int(input('me fale um numero:'))
    cont = cont + 1
    soma = soma + num 
print('o total de numeros digitados foi {} e o total da soma foi {} '.format(cont,soma-999))
