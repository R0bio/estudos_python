'''DESAFIO PROGRESSÃO ARITIMÉTICA'''
termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'. format(c), end= ' -> ')
print('Fim')