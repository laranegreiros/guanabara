peso = float(input(' me fale o seu peso: ')) 
altura = float(input(' me fale a sua altura: ')) 
conta = peso/(altura**2) 
if conta <= 18.5:
    print(' vc esta abaixo do peso ') 
if conta>18.5 and conta<25 and conta>24  : 
    print('vc esta no peso ideal ') 
if conta>25 and conta<30  and conta>29: 
    print(' vc esta com sobrepeso') 
elif conta>30 and conta<40  and conta>39: 
    print('vc esta obeso ')  
if conta<40 : 
    print(' vc esta em obesidade mormida')
