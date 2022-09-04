def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}m x {comp}m é de {a}m².')


print('Controle de Terrenos')
print('--------------------')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
