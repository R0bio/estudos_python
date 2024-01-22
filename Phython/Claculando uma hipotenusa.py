import math
print('Calculadora triangulo retangulo')
op = float(input('Digite o valor correspondente ao Cateto Oposto: '))
ad = float(input('Digite o valor correspondente ao Catedo Adjacente: '))
hi = math.hypot(op,ad)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
