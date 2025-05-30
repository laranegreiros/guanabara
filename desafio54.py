
ano = 2025
maior = 0
menor = 0
for c in range (1,8):
    pe = int(input('me fale a data de nascimento {}:'.format(c)))
    idade = ano - pe 
    if idade < 18 :
        menor = menor + 1
    if idade > 18 :
        maior = maior + 1 
print('o numero de maiores de idade é {} '.format(maior))
print('o numero de menores de idade é de {}'.format(menor))