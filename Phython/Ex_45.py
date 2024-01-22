'''DESAFIO PEDRA PAPEL OU TESOURA'''
# start
import random
print('Jogo JOQUEMPÔ')
print('[1] = Pedra\n[2] = Papel\n[3] = Tesoura')
# user informations
usuario = int(input('Qual a sua escolha? '))
# machine options
lista = (1, 2, 3)
maquina = random.choice(lista)
if maquina ==1:
    print('Escolhi Pedra!')
elif maquina == 2:
    print('Escolhi Papel!')
elif maquina == 3:
    print('Escolhi tesoura!')
# conditions
if maquina == 1 and usuario == 1:
    print('Houve um empate, ambos escolheram Pedra.')
elif maquina == 2 and usuario == 2:
    print('Houve um empate, ambos escolheram Papel.')
elif maquina == 3 and usuario == 3:
    print('Houve um empate, ambos escolheram Tesoura.')
elif maquina == 1 and usuario == 2:
    print('O usuario ganhou, Papel embala Pedra')
elif maquina == 1 and usuario == 3:
    print('A maquina ganhou, Pedra quebra Tesoura.')
elif maquina == 2 and usuario == 1:
    print('O Usuario ganhou, Papel embala a Pedra.')
elif maquina == 2 and usuario == 3:
    print('O usuario ganhou, Tesoura corta Papel.')
elif maquina == 3 and usuario == 2:
    print('A maquina ganhou, Tesoura corta Papel.')
elif maquina == 3 and usuario == 1:
    print('O Usuario ganhou, Pedra quebra Tesoura.')
else:
    print('Jogada invalida.')