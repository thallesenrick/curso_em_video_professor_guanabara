lista = []
lista_pares = []
lista_impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        break
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
print('-=' * 30)
lista.sort()
print(f'A lista completa é {lista}')
lista_pares.sort()
print(f'A lista de pares é {lista_pares}')
lista_impares.sort()
print(f'A lista de impares é {lista_impares}')
