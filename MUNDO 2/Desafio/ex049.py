print('\033[33m''{:=^40}'.format('CALCULADORA AUTOMÁTICA'))
n = int(input('Digite um número para ver sua tabuada: ''\033[m'))
print('\033[34m''_' * 12, '\033[m')
for c in range(1, 11):
    print('\033[32m'f'{n} x {c} = {n*c}')
print('\033[34m''_' * 12, '\033[m')

m = int(input('Digite um número pra ver sua tabuada: '))
for c in range(1, 11):
    print(f'{m} * {c:2} = {m * c}')