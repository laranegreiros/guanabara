import random
n1 = str(input('primeiro aluno: ')) 
n2 = str(input('segundo aluno : ')) 
n3 = str(input('terceiro aluno: ')) 
n4 = str(input('quarto aluno : ')) 
n5 = [n1,n2,n3,n4] 
random.shuffle(n5) 
print('a ordem de apresentasao sera') 
print(n5) 
