from random import randint
c = randint(1,10)
pe = int(input('adivinhe o numero de 1 a 10: '))
contador = 1 
while pe != c :
    print('////tente novamente////')
    pe = int(input('adivinhhe novamente'))
    contador = contador + 1 
print(' vc consequiu! vc tentou {} vezes '.format(contador)) 
