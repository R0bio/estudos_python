'''DESAFIO ESCOLHER UM NOME ALEATORIO'''
import random
print('O professor deseja sortear um aluno aleatorio para apagar o quadro. Vamos ajuda-lo!')
nm1 = str(input('Digite seu nome:'))
nm2 = str(input('Digite seu nome:'))
nm3 = str(input('Digite seu nome:'))
nm4 = str(input('Digite seu nome:'))
lista = (nm1, nm2, nm3, nm4)
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
