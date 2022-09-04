# OPERADORES ARITIMÉTICOS

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite mais um número: '))
# s = n1 + n2
# print('A soma vale {}'.format(s))

# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 ** 2)
# print(5 // 2)
# print(5 % 2)

# ORDEM DE PROCEDÊNCIA
# 1º ()
# 2º **
# 3º *, /, //, %
# 4º +, -

# EXEMPLOS
# print(5+3*2)      (3*5+4**2)       (3*(5+4)**2)
#      (5+6)        (3*5+16)         (3*(9)**2)
#      (11)         (15+16)          (3*(81)
#                   (31)             (243)

# nome = input('Como você se chama? ')
# print('Prazer em te conhecer {:^15}!'.format(nome))

n1 = int(input(' Digite um valor: '))
n2 = int(input(' Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e multi divisão é {:.2f}.'.format(s, m, d), end= ' ')
print('Divisão inteira {} e potência {}'.format(di, e))
