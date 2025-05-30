pergunta= input('digite algo : ').upper() 
print(' sua frase tem {} letras a'.format(pergunta.count('A'))) 
print(' ela aparece primeiro na posição {}'.format(pergunta.find('A')+1))  
print(' ela aparece na ultima vez na posição {}'.format(pergunta.rfind('A')+1))
