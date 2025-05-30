pergunta = float(input ('me fale a distansia: ')) 
if pergunta<= 200:
    print('sua corrida vai ser {:.2f} reais'.format(pergunta*0.50))
else:
    print('sua corrida vai ser {:.2f} reais'.format(pergunta*0.45)) 