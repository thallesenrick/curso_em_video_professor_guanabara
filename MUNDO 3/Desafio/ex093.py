dados = dict()
lista = list()
dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c+1}? ')))
dados['gols'] = lista[:]
dados['total'] = sum(lista)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   => Na partida {c+1}, fez {dados["gols"][c]} gols.')
print(f'Foi um total de {dados["total"]} gols.')
