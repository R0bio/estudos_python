'''DESAFIO TABUADA'''
print('Tabuada em Python.')
print('-='* 8)

while True:
    
    user = str(input('Voce quer continuar ? [S/N]')).upper()
    if user == 'N':
        break
    
    num = int(input('Digite um numero:'))    
    r1 = (num*1)
    r2 = (num*2)
    r3 = (num*3)
    r4 = (num*4)
    r5 = (num*5)
    r6 = (num*6)
    r7 = (num*7)
    r8 = (num*8)
    r9 = (num*9)
    r10 = (num*10)
    
    print(f'O resultado é \n {num} X 1 = {r1}\n {num} X 2 = {r2}\n {num} X 3 = {r3}\n {num} X 4 - {r4}\n {num} X 5 = {r5}\n {num} X 6 = {r6}\n {num} X 7 = {r7}\n {num} X 8 = {r8}\n {num} X 9 = {r9}\n {num} X 10 = {r10}')

