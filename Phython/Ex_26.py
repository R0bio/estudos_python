'''DESAFIO PROCURANDO POR UMA LETRA'''
frase = str(input('Digite sua frase: ')).lower().strip()
print('A letra A aparece {} vezes dentro da frase.'.format(frase.count('a')))
print('A letra A aparece na {} posição da frase.'.format(frase.find('a')+1))
print('A ultima posição em que aparece a letra A é na {}'.format(frase.rfind('a')+1))
