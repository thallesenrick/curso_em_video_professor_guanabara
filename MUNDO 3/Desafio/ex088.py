from random import randint
from time import sleep
lista = []
jogos = []
print(f'\033[92m-' * 30)
print(f'{"$$ JOGA NA MEGA SENA $$":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('...' * 2, f'SORTEANDO {quant} JOGOS', '...' * 2)
for i, jogos in enumerate(jogos):
    print(f'\033[91mJogo {i + 1}: {jogos}')
    sleep(1)
print(f'\033[92m.....' * 2, 'BOA SORTE', '.....' * 2)