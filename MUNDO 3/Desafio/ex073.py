times = ('América-MG', 'Athletico-PR', 'Atlético Goianiense',
         'Atlético Mineiro', 'Avaí', 'Botafogo', 'Ceará',
         'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Goias', 'Internacional',
         'Juventude', 'Palmeiras', 'Bragantino', 'Santos',
         'São Paulo')
print('-=-' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=-' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=-' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=-' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 15)
print(f'O Ceará está na {times.index("Ceará") + 1}ª posição.')
