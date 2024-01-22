resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('Acabou')