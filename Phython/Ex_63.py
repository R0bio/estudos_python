print('=-'* 11)
print('Sequência de Fibonacci')
print('=-'* 11)
n = int(input('Quantos termos voce quer mostrar:'))
termo_1 = 0
termo_2 = 1
print('※'* 22)
print('{} → {}'.format(termo_1, termo_2))
cont = 3
while cont <= n:
    termo_3 = termo_1 + termo_2
    print(' → {} '.format(termo_3), end='')
    termo_1 = termo_2
    termo_2 = termo_3
    cont +=1
print('Fim.')

