'''DESAFIO MEDIA ESCOLAR DO ALUNO'''
print('Bem vindo a sua calculadora de media escolar')
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print('Parabens voce foi aprovado!')
else:
    print('Infelizmente voce reprovou!')
