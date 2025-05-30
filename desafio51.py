print(' /////10 TERMOS DE UMA PA///// ')
termo = int(input('primeiro termo: '))
razão = int(input('razão: '))
decimo = termo + (10 - 1) * razão
for c in range (termo,decimo+1,razão):
    print(c)
print('FIM')
