from math import floor, trunc
n = float(input('Digite um número: '))
a = floor(n)
print(f'O número digitado foi {n} e a sua porção inteira é {a}.')

m = float(input('Digite outro número: '))
b = trunc(m)
print(f'O número digitado foi {m} e a sua porção inteira é {b}.')

o = float(input('Digite mais um número: '))
print(f'O número digitado foi {o} e a sua porção inteira é', int(o))
