soma = 0
cont = 0
for c in range (1,7):
   pe = int(input(' me fale um numero 6/{}: '.format(c)))
   if pe % 2 == 0 :   
    cont+=1
    soma+=pe
print('vc digitou {} numeros pares e a soma deles é {}'.format(cont,soma))

 