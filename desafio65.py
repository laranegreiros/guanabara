num = int(input('digite um numero: '))
co = str(input('deseja continuar?(S/N)')).upper()
maior = 0
menor = 0 
cont = 0
while co == 'S':
    num = int(input('digite um numero:'))
    co = str(input('deseja continuar?(S/N)')).upper()
    cont = cont + 1
    if cont == 1 :
        maior = num 
        menor = num
    if cont > 1 :
        if num > maior:
            maior = num 
            menor = menor
print('o maior numero foi {} e o menor foi {}'.format(maior,menor))
     
 