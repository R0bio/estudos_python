'''DESAFIO RADAR DE VELOCIDADE'''
print('Radar de velcidade 80Km/h')
velocidade = int(input('Qual a velocidade registrada? '))
if velocidade > 80:
    print('Veiculo ultrapassou o limite de velocidade e foi multado.')
    multa = (velocidade - 80) * 7
    print('O valor da multa foi {:.2f}'.format(multa))
else:
    print('Veiculo está dentro do limite de velocidade.')
