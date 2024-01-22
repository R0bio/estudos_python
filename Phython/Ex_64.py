num = 0
cont = 0
soma = 0
num = int(input('Digite um numero. '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero. '))

print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))