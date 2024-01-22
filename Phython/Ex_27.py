'''DESAFIO PRIMEIRO E ULTIMO NOME'''
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Olá, muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
