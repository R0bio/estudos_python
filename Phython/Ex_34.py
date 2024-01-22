'''DESAFIO AUMENTO DE SÁLARIO'''
salario = float(input('Digite seu salário: '))
if salario <= 1250:
    resultado = salario + (salario * 15 / 100)
else:
    resultado = salario + (salario * 10 / 100)
print('Você recebeu um aumento. Seu salário agora é R${:.2f}'.format(resultado))
