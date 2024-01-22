'''FDESAFIO HIPOTENUSA'''
import math
print('Oi, bem vindo a ferramenta de calculo da Hipotenusa!')
a = float(input('Digite o comprimento do cateto adjacente: '))
o = float(input('Digite o comprimento do cateto oposto: '))
h = math.hypot(a,o)
print('A hipotenusa é: {:.2f}'.format(h))