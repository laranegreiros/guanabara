n1 = float(input(' qual o valor do emprestimo ? '))
n2 = float(input(' quanto vc ganha ? '))
n3 = int(input(' em quanto tempo pretende pagar ?'))
a = n3 * 12
b = n2/a 
c = (n2 * 30)/100
if b> c :
    print ( ' não será possivel evetuar o imprestimo')
elif b== c :
    print( '  será possivel ,vc pagara {} reais por {} meses  '.format(b , a))
else:
    print (' será possivel , vc pagará {} reais por {} meses'.format(b , a) )