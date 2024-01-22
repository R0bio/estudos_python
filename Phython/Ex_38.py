'''DESAFIO NUMEROS MAIORES E MENORES'''
print('Sistema de identificação de numeros')
num_1 = int(input('Insira o primeiro numero: '))
num_2 = int(input('Insira o segundo numero: '))
if num_1 > num_2: 
    print('O primeiro valor de "{}" é maior!'.format(num_1))
elif num_1 == num_2:
    print('Os dois valores são iguais')
else:
    print('O segundo valor de "{}" é maior!'.format(num_2))
    