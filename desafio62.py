term1 = int(input('digite o primeiro termo do PA: '))
raz = int(input('digite a razão: '))
term = term1
cont = 1
total = 0
mais = 10
while mais != 0 :
   total = total + mais
   while cont <= total:
     print('{}'.format(term),end='-')
     term = term + raz
     cont = cont + 1
   print('pausa')
   mais = int(input('quantos termos vc quer mostrar a mais? '))
print('o numero de termos foi de {}'.format(total))
print('FIM')