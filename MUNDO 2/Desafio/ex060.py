# USANDO WHILE
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! ->', end=' ')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

# USANDO FOR
m = 1
numero = int(input('Digite um número para calcular seu Fatorial: '))
print(f'Calculando {numero}! ->', end=' ')
for c in range(numero, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    m *= c
print(m)