'''DESAFIO REAL X DOLAR'''
print('Ola, bem vindo ao aroporto Robio - Airlines \n Esse e o seu app de cambio de moeda.')
real = float(input('informe a quantidade de Reais (.BRL):'))
dolar = 5.16
print('hoje 1 Dolar esta custando',dolar,'R$')
res = real / dolar
print('Voce comprou USD {:.2f} Boa viagem!'.format(res))
