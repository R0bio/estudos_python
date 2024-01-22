'''DESAFIO SENO COSSENO E TANGENTE'''
from math import hypot
op = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto Adjacente: '))
hip = hypot(op,ad)
print ('O comprimento da Hipotenusa é: {:.2f}'.format(hip))
