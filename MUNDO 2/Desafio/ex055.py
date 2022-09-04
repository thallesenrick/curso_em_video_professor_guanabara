lista = []
for c in range(1, 6):
    peso = float(input('\033[93m'f'Peso da {c}ª pessoa: '))
    lista += [peso]
print('\033[94m'f'O maior peso lido foi de {max(lista)}Kg!')
print('\033[91m'f'O menor peso lido foi de {min(lista)}Kg!')


maior = 0
menor = 0
for p in range(1, 6):
    pes = float(input('\033[93m'f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = pes
        menor = pes
    else:
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
print('\033[94m'f'O maior peso lido foi de {maior}Kg!')
print('\033[91m'f'O menor peso lido foi de {menor}Kg!')
