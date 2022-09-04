viagem = float(input('Qual é multi distância da sua viagem? '))
print(f'Você está prestes multi começar uma viagem de {viagem:.1f}Km.')
if viagem <= 200:
    print(f'E o preço da sua passagem será de R${viagem * 0.50:.2f}')
else:
    print(f'E o preço da sua passagem será de R${viagem * 0.45:.2f}.')

# preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
# print(f'Sua passagem vai custar R${preco}')
