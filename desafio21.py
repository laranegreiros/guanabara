pergunta = str(input('me fale algo')).strip()
print('sua frase em maiuscula e {}'.format(pergunta.upper()))
print('sua frase em minusculo e {}'.format(pergunta.lower())) 
print(' ela tem ao todo {} letras'.format(len(pergunta)))
separa = pergunta.split()
print('a primeira palavra e {} ela tem {} letras'.format(separa[0],len(separa[0])))

