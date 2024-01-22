'''DESAFIO INFORMAR O NUMERO PRIMO'''
print('Checador de numero primo')
num = int(input('\nDigite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO numero {}, foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Por isso o numero {} é primo!'.format(num))
else: 
    print('Por isso o numero {} não é primo!\n'.format(num))
