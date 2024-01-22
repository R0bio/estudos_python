'''DESAFIO TRABALHANDO COM STRINGS '''
print('Bem vindo ao seu App de conversão de caracteres')
nome = str(input('Digite seu nome completo: ')).strip()
print('Estou analisando seu nome...')
print('Seu nome em maiusculo fica: {}'.format(nome.upper()))
print('Seu nome em minusculo fica: {}'.format(nome.lower()))
print('Seu nome ao todo tem: {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem: {}'.format(nome.find(' ')))
print('Seu nome captalizado fica: {}'.format(nome.capitalize()))

#FOMATANDO UMA FRASE INTEIRA#