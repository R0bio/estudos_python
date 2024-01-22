'''DESAFIO JOGO DA ADIVINHACAO'''
import random
lista = (1,2,3,4,5,6,7,8,9,10)
print('Escolha um numero de 1 a 10!')
numero_escolhido = random.choice(lista)
escolhido_usuario = int(input('Qual numero eu escolhi? '))
if escolhido_usuario == numero_escolhido:
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez!')
