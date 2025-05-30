mulher = 0
soma = 0
media = 0
homem = 0
nomehomem = 0
for c in range (1,5):
    print('pessoa {}'.format(c))
    nome = str(input(' nome: '))
    idade = int(input('idade: '))
    genero = str(input('genero(f/m: '))
    soma = idade + soma 
    if genero == 'm' and homem == 0 and nomehomem == 0 :
        homem = idade 
        nomehomem = nome 
        if idade > homem :
            homem == idade 
            nomehomem == nome 
    if genero == 'f' and idade < 20:
        mulher = + 1
media = soma / 4
print('a média de idade é {}'.format(media))
print(' o homem mais velho é o {} , ele tem {} anos '.format(nomehomem,homem))
print('o numero de mulhares com menos de 20 anos é de {}'.format(mulher))
