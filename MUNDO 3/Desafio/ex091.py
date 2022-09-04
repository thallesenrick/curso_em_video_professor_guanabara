from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
sleep(1)
for k, v in jogadores.items():
    print(f'\033[93mO {k} tirou [{v}] no dado.')
    sleep(1)
print(f'\033[m{"-=" * 30}')
print('  == RANKING DOS JOGADORES == ')
sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'\033[94m    {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
