'''DESAFIO APLICAR 5% OFF'''
print('Oi, bem vindo a sua calculadora de descontos.')
valor_original = float(input('Digite o valor total '))
valor_descontado = valor_original * 0.005
novo_valor = valor_original * 0.95
print('O total de: {} com desconto de 5% é: {:.2f}.'.format(valor_original,novo_valor,))