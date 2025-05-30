valor = float(input(' digite o valor do produto: ')) 
print(''''formas de pagamento
[1] dinheiro
[2] cheque 
[3] cartão a vista
[4] 2 vezes no cartão 
[5] 3 ou mais vezes no cartão''')
forma = int(input('digite a forma de pagamento: ')) 
if forma == 1 or forma == 2 : 
    print(' vc pagará {:.2f} reais'.format(valor-(valor*10/100))) 
elif forma == 3 : 
    print('vc pagará {:.2f} reais'.format(valor-(valor*5/100))) 
if forma == 4 : 
    print(' vc pagará {:.2f} reais'. format(valor)) 
elif forma == 5 : 
    print(' vc pagará {:.2f} reais'.format(valor+(valor*20/100))) 

