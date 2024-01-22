'''DESAFIO ALUGUEL DE CARROS'''
print('Aluguel de carros.')
dias = int(input('Quantos dias ficou com o carro?'))
km = float(input('Percorreu quantos Km?'))
v1 = dias * 60
v2 = 0.15 * km
resultado = v1 + v2
print('O alugem custou o total de:{:.2f}'.format(resultado))