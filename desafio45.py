from random import randint
print(' VAMOS JOGAR PEDRA , PAPEL E TESOURA')
itens = ('papel','pedra','tesoura')
pc =  randint(0,2)
print(''' VEJA O Q VC PODE ESCOLHER 
[0] PAPEL
[1]PEDRA
[2]TESOURA''') 
escolha = int(input(' digite o numero desejado: ')) 
print(' vc escolheu {}'.format(itens[escolha]))
print(' eu joquei {}'.format(itens[pc]))
if pc == 0:
    if escolha == 0 :
        print(' deu empate ')
    if escolha == 1 :
        print(' eu ganhei!')
    else:
        print(' vc ganhou')
elif pc == 1:
    if escolha == 0 :
        print(' eu perdi')
    elif escolha == 1 :
        print('deu empate') 
    else:
        print('eu ganhei!')
if pc == 2:
    if escolha == 0 :
        print(' eu ganhei!')
    elif escolha == 1 : 
        print(' vc ganhou')
    else: print(' deu empate')
else:
    print (' opção invalida')
