soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f'A soma de todos os {contador} valores é {soma}.')


som = 0
con = 0
for n in range(0, 1000):
    if n % 5 == 0:
        som += n
        con += 1
print(f'A soma de todos os {con} valores é {som}.')