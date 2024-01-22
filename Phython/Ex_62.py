print('Gerador de PA')
print ('-=' * 10)
primeiro_Termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro_Termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais?: '))
print('Progressao finalizada com {} termos mostrados.'.format(total))