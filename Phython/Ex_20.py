'''DESAFIO EMBARALHAR ALUNOS'''
from random import shuffle
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))
resultado = [n1, n2, n3, n4]
shuffle (resultado)
print('A ordem de apresentacao sera: ')
print(resultado)
