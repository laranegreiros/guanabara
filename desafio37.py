n1 = int(input(' me fale um numero : '))
print('vc pode converter para  1) binario 2)octal 3)hexadecimal')
n3 = int(input(' me fale a opção '))
if n3 == 1 :
    print(' o numero {} em binario é {}'.format(n1,bin(n1)))
elif n3 == 2:
    print(' o numero {} em octal é {}'.format(n1,oct(n1)))
elif n3 == 3:
    print(' o numero {} em hexadecimal é {}'.format(n1,hex(n1)))
else:
    print('opsão invalida')
