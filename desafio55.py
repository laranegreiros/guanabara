menor = 0
maior = 0
for c in range (1,6):
    pe = float(input('me fale seu peso pessoa {}:'.format(c)))
    if c == 1 :
        maior = pe
        menor = pe 
    else:
        if maior < pe :
            maior = pe 
        if menor > pe :
            menor = pe 
print(' o maior peso foi {}'.format(maior))
print(' o menor peso foi {}'.format(menor))
