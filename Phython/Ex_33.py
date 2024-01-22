'''DESAFIO MAIOR E MENOR VALOR'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('terceiro valor: '))
#Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('o menor valor digitado foi o {}'.format(menor))
#Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi o {}'.format(maior))
