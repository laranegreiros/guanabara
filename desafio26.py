pergunta = input(' digite o deu nome : ').strip()
separa = pergunta.nsplit()  
print(' seu nome é {}'.format(separa[0])) 
print (' seu ultimo sobrenome é : '.format(separa[len(separa)-1]))