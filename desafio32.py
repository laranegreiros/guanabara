pergunta = int(input(' me fale um ano :')) 
if pergunta %4 == 0 and pergunta % 100  == 0 and pergunta % 400 == 0:
    print(' o ano {} é bixessesto'.format(pergunta)) 
else:
    print('o ano {} não é bixessesto'.format(pergunta))