num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print('\n\033[m'f'O número {num} foi dividido {cont} vezes.')
if cont == 2:
    print('Logo É um número PRIMO!')
else:
    print('Logo NÃO É um número PRIMO!')
