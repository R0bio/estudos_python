'''DESAFIO JOGO DA ADIVINHACAO V2'''
import random
print('TENTE ADIVINHAS O NUMERO! ')
lista = 1,2,3,4,5,6,7,8,9,10
maquina = random.choice(lista)
usuario = int(input('ESCOLHA UM NUMERO DE 1 A 10 '))
tentativa = 0 
while usuario != maquina:
   tentativa += 1
   usuario = int(input('ERROU, TENTE NOVAMENTE: '))
print('VOCE ACERTOU. O NUMERO ESCOLHIDO FOI {}'.format(maquina))
print('O NUMERO DE TENTATIVAS FOI {}'.format(tentativa))
