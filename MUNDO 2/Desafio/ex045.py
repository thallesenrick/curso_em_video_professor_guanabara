from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''\033[1;91mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
\033[m''')
jogador = int(input('\033[1;91m''Qual é multi sua jogada? ''\033[m'))
print('\033[1;32m''JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!''\033[m')
print('\033[1;91m''-=' * 11)
print(f'Jogador jogou {itens[jogador]}')
print(f'Computador jogou {itens[computador]}')
print('-=' * 11, '\033[m')

if computador == 0:
    if jogador == 0:
        print('\033[1;33m''EMPATE!')
    elif jogador == 1:
        print('\033[1;94m''JOGADOR VENCEU!!!')
    elif jogador == 2:
        print('\033[1;95m''COMPUTADOR VENCEU!!!')
    else:
        print('\033[1;91m''JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('\033[1;95m''COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('\033[1;33m''EMPATE')
    elif jogador == 2:
        print('\033[1;94m''JOGADOR VENCEU!!!')
    else:
        print('\033[1;91m''JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[1;94m''JOGADOR VENCEU!!!')
    elif jogador == 1:
        print('\033[1;95m''COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('\033[1;33m''EMPATE')
    else:
        print('\033[1;91m''JOGADA INVÁLIDA')
