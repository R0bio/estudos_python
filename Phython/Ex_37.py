'''DESAFIO BASE NUMERICA'''
print('Conversor pare numeracao de maquina')
print('[1] = BINARIO\n[2] = OCTAL\n[3] = HEXADECIMAL')
numero = int(input('Digite um numero: '))
escolha = int(input('Selecione a opção de conversão: '))
if escolha == 1:
    print('Resultado: {}'.format(bin(numero)[2:]))
elif escolha == 2:
    print('Resultado: {}'.format(oct(numero)[2:]))
elif escolha == 3:
    print('Resultado: {}'.format(hex(numero)[2:]))
else:
    print('Opcão inválida!')
