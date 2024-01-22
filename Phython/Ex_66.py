num = 0
soma =5
while True:
    num = int(input('Digite um numero.'))
    if num == 999:
        break
    soma += num
print(f'A soma dos numeros é de {soma}')
