'''DESAFIO ENCONTRAR O MAIOR E MENOR VALOR EM IDADE'''
from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(total_maior))
print('E tivemos o total de {} pessoas menores de idade.'.format(total_menor))
