pergunta1 = int(input(' me fale um  numero :')) 
pergunta2 = int(input('me fale outro numero :')) 
pergunta3 = int(input('me fale o ultimo numero: '))
menor = pergunta1 
if pergunta2 < pergunta1 or pergunta2 < pergunta3:
    menor = pergunta2
if pergunta3 < pergunta2 or pergunta3 < pergunta1:
    menor = pergunta3 
if pergunta1< pergunta2 or pergunta1<pergunta3:
    menor = pergunta1
maior = pergunta1
if pergunta2 > pergunta1 or pergunta2 > pergunta3:
    maior = pergunta2 
if pergunta3 > pergunta1 or pergunta3 > pergunta2:
    maior = pergunta3
print('o maior valor é o {}'.format(maior)) 
print('o menor valor é o {} '.format(menor))


     