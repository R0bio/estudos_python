'''DESAFIO LER IDADE DO ATLETA'''
print('Calcular idade do atleta')
idade = int(input('Informe a sua idade: '))
if idade <= 9:
    print('Mirim.')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Senior')
elif idade > 20:
    print('Master')