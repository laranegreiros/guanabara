l1 = float(input(' me fale um lado do triangulo: ')) 
l2 = float(input(' me fale o ultimo lado: ')) 
l3 = float(input(' me fale  ultimo lado: ')) 

if l1< l2 + l3 and l2< l1 + l3 and l3< l1 + l2 : 
    print('vc pode formar um triangulo  ' , end='')
    if l1 == l2 == l3 :
        print(' ele é um equilatero ') 
    elif l1 != l2 != l3 != l1 : 
        print( ' ele é um escaleno') 
    else : 
        print('ele é um isoselis ')
else:
    print(' vc não consegue ') 


