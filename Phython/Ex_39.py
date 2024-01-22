'''DESAFIO ALISTAMENTO MILITAR'''
print('Ola, bem vindo ao sistema de alistamento militar Brasileiro!')
nome = str(input('Digite seu nome: '))
genero = str(input('Digite seu genero: ')).lower()
idade = int(input('Digite sua idade: '))
if genero == 'masculino' and idade == 18:
    print('Voce esta apto a realizar o alistamento militar.')
elif genero == 'feminino':
    print('Você não está apta a realizar o alistamento militar :')
elif idade > 18:
    print('O prazo para voce se alistar ja passou.')
elif idade < 18:
    print('Voce ainda nao precisa se alistar.')