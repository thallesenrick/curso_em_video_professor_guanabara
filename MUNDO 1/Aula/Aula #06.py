# DADOS PRIMITIVOS

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2

print('A soma vale', s)
print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

n3 = int(input('Digite um valor: '))
n4 = int(input('Digite outro valor: '))
s = n3 + n4
print('A soma vale', s)

print(f'A soma entre {n3} e {n4} vale {s}')
print('A soma entre {}'.format(n3), 'e {}'.format(n4), 'vale {}'.format(s))
# print('A soma entre', n1, 'e', n2, 'vale', s) método antigo
print('A soma entre {} e {} vale {}'.format(n3, n4, s))

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
n = (input('Digite algo: '))
print(n.isalpha())  # Para letras
print(n.isnumeric())  # Para Números
print(n.isalnum())  # Para números e letras
print(n.isupper())  # Para letras maiúsculas
print(n.islower())  # Para letras minúsculas
print(n.isprintable())  # Para saber se pode ser impresso

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# DESAFIO

algo1 = int(input('Digite um número: '))
algo2 = int(input('Digite outro número: '))
s = algo1 + algo2
print('A soma entre {} e {} é igual {}!'.format(algo1, algo2, s))

