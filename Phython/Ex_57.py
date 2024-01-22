'''EXERCICIO DE LER O SEXO DO CLIENTE'''
print('Coletor de dados')
nome = str(input('Informe seu nome: ')).capitalize()
sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe o sexo: [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Ola senhor {}, seja bem vindo!'.format(nome))
else:
    print('Ola senhora {}, seja bem vinda!'.format(nome))
