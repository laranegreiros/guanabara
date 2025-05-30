frase  =  str(input(' me fale uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
sep = junto[::-1]
print(' essa frase {} ao contrario é {}'.format(junto , sep ))
for letra in range (len(junto) - 1, -1 , -1):
    sep += junto[letra] 
if sep == junto  :
    print('é um palindromo ')
else :
    print(' essa frase não é um palidromo')



