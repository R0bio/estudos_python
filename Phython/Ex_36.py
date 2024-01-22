'''DESAFIO FINANCIAMENTO DA CASA'''
print('Bem vindo ao Banco Caixa!')
home_price = float(input('Informe o valor a ser financiado: '))
payment_value = float(input('Informe o seu rendimento mensal: '))
amount_paymnet = int(input('Informe a quantidade de parcelas: '))
payment_percent = (payment_value* 30 /100)
partion_price = (home_price / amount_paymnet)
print('Valor total do imovel: R${}\nTotal de parcelas solicitadas: {}\nValor total de cada parcela: R${:.2f}'.format(home_price,amount_paymnet,partion_price))
if partion_price < payment_percent:
    print('O imovel pode ser financiado.')
else:
    print('O imovel não pode ser financiado. Aumente o numero de parcelas!')
    