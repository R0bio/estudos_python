'''DESAFIO CALCULADORA DE NUMEROS IMPARES MULTIPLOS DE 3'''
print('Calculadora de numeros impares multiplos de 3 em um espaco entre 0 a 500.')
soma = 0
contador =  0
for count in range(1, 501, 2):
    if count % 3 ==0:
       contador = contador + 1
       soma = soma + count
print('A soma dos {} contadores informados é de {}.'.format(contador, soma))
