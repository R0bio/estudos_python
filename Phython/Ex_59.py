n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:

    print('''  
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção?: '))
    
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado da multiplicação de {} X {} é {}'.format(n1, n2, produto) )
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre o numero {} e o numero {} o {} é o maior.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando programa.')
    else:
        print('Opção inválida, tente novamente!')
print('Fim do programa!')
