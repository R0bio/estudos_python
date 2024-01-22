'''PRIMEIRO CODIGO'''
#Apresentação
from datetime import datetime
print('CALCULADORA')
#Coleta de dados
salario = float(input('Quanto você ganha por mês? '))
horas = float(input('Quantas horas trabalha por dia? '))
dias = int(input('Quantos dias irá trablhar esse mês? '))
#Sistema de cálculo
horas_mensais = (dias * horas)
valor_hora = (salario / horas_mensais)
valor_dia = (valor_hora * horas)
horas_anuais = (horas * 252)
valor_minuto = (valor_hora / 60)
agora = datetime.today()
depois = datetime (2022, 3, 16, 17, 45, 00)
dif = depois - agora
#Resposta ao usuário
print('Considerando que você trabalhará {:.2f} horas este mês'.format(horas_mensais))
print('Cada minuto do seu trabalho custará R${:.5f}'.format(valor_minuto))
print('Cada hora do seu trabalho custará R${:.2f}'.format(valor_hora))
print('cada dia do seu trabalho custará R${:.2f}'.format(valor_dia))
print ('Restam exatamente {} para acabar o expediente'.format(dif))
#final
