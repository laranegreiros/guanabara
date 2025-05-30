dia = int(input(' me fale o seu dia de nascimento:'))
mes = int(input('me fale o mes :')) 
ano = int(input(' me fale o ano :'))
conta = 2024 - ano
if conta == 18 and mes == 12 and dia == 27:
    print(' já é hora ')
elif conta> 18 and mes> 12 and dia> 27 :
    print(' já passou do tempo ')
if conta== 18 and mes<12 and dia< 27:
    print('ainda falta {} dias e {} meses '.format(dia- 27 , 12-mes)) 
elif conta< 18 and mes<12 and  dia<27 : 
    print(' ainda falta {} anos , {} meses e {} dias'.format( 18 - conta , mes - 12 , dia - 27))
