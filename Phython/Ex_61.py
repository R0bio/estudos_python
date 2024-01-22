print('Gerador de PA')
print ('-=' * 10)
primeiro_Termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro_Termo
cont = 1
while cont <=10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')