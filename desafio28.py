from random import randint  
computador = randint(0,5)
pergunta=int(input('em que numero estou pensando ? ')) 
if computador==pergunta:
    print( 'vc ganhou o numero era{} '.format(pergunta))
else:
    print('vc perdeu o numero era {}'.format(computador))




