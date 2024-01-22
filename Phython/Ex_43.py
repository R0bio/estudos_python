'''DESAFIO INDICE DE MASSA CORPORAL'''
print('Programa para calcular o indece de massa corporal')
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = ( peso / (altura * altura))
print('Seu IMC é: {:.1f} '.format(imc))
if imc < 18.5:
    print('Magreza')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 39.9:
    print('Obesidade')
elif imc >= 40.0:
    print('Obesidade morbida')
