'''DESAFIO PRECO DA PASSAGEM'''
distancia = float(input('Digite a distancia da viagem: '))
if distancia > 200:
    valor_longa = (distancia * 0.45)
    print('Uau, que viagem longa!\nO valor da passagem é {:.2f}'.format(
        valor_longa))
else:
    valor_curta = (distancia * 0.50)
    print('O valor da passagem é: {:.2f}'.format(valor_curta))
print('Tenha um boa viagem!')
