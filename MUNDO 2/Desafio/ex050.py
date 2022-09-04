soma = 0
contador = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma += n
        contador += 1
print(f'A soma de todos os {contador} valores pares é {soma}. ')

som = 0
cont = 0
for c in range(1, 7):
    m = int(input(f'Digite o {c}º número: '))
    if m % 2 == 0:
        som += m
        cont += 1
print(f'A soma de todos os {cont} valores pares é {som}.')
