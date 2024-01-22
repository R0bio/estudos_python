import random
print('\nJogo do par ou impar!\n')
user = 0
soma = 0
while True:
    if user == 3:
        break
    lista = (1,2)
    user = int(input('[1] Cara\n[2] Coroa\n[3] para sair\n\nDigite:'))
    maquina = random.choice(lista)
    if user == maquina:
        print('Parabens voce ganhou!')
        soma = soma + 1
    if user != maquina:
        print('Voce perdeu!')
print('\nJogo Finalizado!\n')
print(f'Voce fez {soma} pontos.')

