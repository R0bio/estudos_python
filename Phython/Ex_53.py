'''DESAFIO ENCONTRAR UM PALINDROMO'''
frase = str(input('Digite sua frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(' A frase "{}" se invertido fica "{}"'.format(junto,inverso))
if inverso == junto:
    print('Opa, temos um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')

