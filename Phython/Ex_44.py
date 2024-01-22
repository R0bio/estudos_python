'''DESAFIO MAQUINA DE CARTAO'''
print('Opcoes de pagamento ponto de venda.')
valor_original = float(input('Informe o valor do produto: '))
#PAGAMENTO EM DINHEIRO 10% OFF
dinheiro = (valor_original * 10 / 100 )
dez_por_cento = (valor_original - dinheiro)
#PAGEMTNO NO CARTAO DE DEBITO 5%OFF
debito = (valor_original * 5 / 100 )
cinco_por_cento = (valor_original - debito)
#PAGAMENTO CREDITO A VISTA 0%OFF
credito_vista = valor_original 
#PAGAMENTO PARCELADO + 10%
acrescimo =  valor_original + (valor_original * 10 / 100) 
#IDENTIFICANDO O TIPO DE PAGAMENTO
escolha = int(input('Informe a forma de pagamento\n1 = Dinheiro\n2 = Cartão\n3 = Crédito à vista\n4 = Crédito parcelado\n Digite a forma de pagamento: '))
if escolha == 1:
    print('Valor total {:.2f}'.format(dez_por_cento))
elif escolha ==2:
    print('Valor total {:.2f}'.format(cinco_por_cento))
elif escolha == 3:
    print('Valor total {:.2f}'.format(credito_vista))
elif escolha ==4:
    print('Valor total {:.2f}'.format(acrescimo))
