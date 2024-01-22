'''DESAFIO MEDIA DE PONTOS'''
print('Faculdade estadual do condado de Ohio')
nome = input('Digite seu nome: ')
print('Olá', nome, 'seja bem vindo!')
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
print('Informamos que para ser aprovado será nescessário uma média de 6.0')
resultado = (primeira_nota + segunda_nota + terceira_nota) / 3
print('O seu resultado foi {:.1f}' .format(resultado))
if resultado >= 6.0:
    print('Parabéns', nome, 'você foi aprovado!')
else:
    print('Sentimos muito, mas não foi dessa vez!')
