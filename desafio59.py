num1 = int(input('me fale um numero: '))
num2 = int(input('me fale outro numero: '))
print('escolha a forma ' \
'[1]somar' \
'[2]multiplicar' \
'[3]maior' \
'[4]novos numeros'
'[5] sair do progama') 
per = int(input('digite a forma: ')) 
if per == 1 :
    print('a soma dos numeros é {}'.format(num1+num2))
if per == 2 :
    print('a multiplicaçao dos numeros é {}'.format(num1*num2))
if per == 3 : 
    if num1 > num2 :
        print('o maior numero é '.format(num1))
    elif num1 < num2 :
        print(' o maior numero é {}'.format(num2))
if per == 5 :
    print('obrigado')
con = str(input(' deseja continuar(s/n)??')).upper() 
while con != 'N': 
    num1 = int(input(' me fale um numero: '))
    num2 = int(input('me fale outro numero: '))    
    print('escolha a forma ' \
'[1]somar' \
'[2]multiplicar' \
'[3]maior' \
'[4]novos numeros'
'[5] sair do progama') 
    per = int(input('digite a forma '))
    if per == 1 :
       print('a soma dos numeros é {}'.format(num1+num2))
    if per == 2 :
       print('a multiplicaçao dos numeros é {}'.format(num1*num2))
    if per == 3 : 
       if num1 > num2 :
        print('o maior numero é '.format(num1))
    elif num1 < num2 :
        print(' o maior numero é {}'.format(num2))
    if per == 5 :
       print('obrigado')
    con = str(input(' deseja continuar(s/n)??')).upper()
print('vc ajudou muito')