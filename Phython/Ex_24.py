'''DESAFIO ANALISE DE STRING PRIMEIRA PALAVRA'''
from pickle import FALSE
cid = str(input('Em que cidade voce nasceu? ')).strip()
res = (cid[1:5].upper() == 'SANTO')
if res == False:
    print('Sua cidade nao tem santo no nome')

