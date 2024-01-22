'''DESAFIO REFAZER O EXERCICIO DA CALCULADORA'''
print('Sistema universal de tabuada.')
num = int(input('Digite um numero: '))
for count in range (1, 11):
    print('{} x {:2} = {}'.format(num, count, num*count))
