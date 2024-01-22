'''DESAFIO TIPOS PRIMITIVOS'''
palavra = input('Digite algo!')
print('O tipo primitivo desse valor é', type(palavra))
print('Só tem espaços?', palavra.isspace())
print('É um numero?', palavra.isnumeric())
print('E alfa numerico?', palavra.isalpha())
print('Esta em maisculo?', palavra.isupper())
print('Esta em minuscolo?', palavra.islower())
print('Esta em minuscolo?', palavra.istitle())