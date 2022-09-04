n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))

# MÉTODO 1
print(f'O menor valor digitado foi {min(n1, n2, n3)}')
print(f'O maior valor digitado foi {max(n1, n2, n3)}')

# MÉTODO 2
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

# MÉTODO 3
me = n1
if n2 < n1 and n2 < n3:
    me = n2
elif n3 < n1 and n3 < n2:
    me = n3
print(f'O menor valor digitado foi {me}')

ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
elif n3 > n1 and n3 > n2:
    ma = n3
print(f'O menor valor digitado foi {ma}')
