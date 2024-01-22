print('Olá, você está utilizando a central de cambio de moedas do aeroporto internacional Robio Airlines')
print('Hoje o Dolar(USD) está cotado a R$5.01')
valor = float(input('Digite a quantidade de Reais(BRL) disponiveis: '))
dolar = 5.01
resultado = valor / dolar
print('Informamos que o valor de R${:.2f}  equivale a US{:.2f}\nGostaria de continuar com a compra?' .format(valor,resultado))
escolha = int(input('Para continuar tecle 1: \nPara cancelar tecle 2:\n'))
if escolha == 1:
    print('Operação registrada com sucesso.')
else:('Operação cancelada.')
print('Obrigado por ultilizar os sistema de combio Robio, tenha uma excelente viagem!')


