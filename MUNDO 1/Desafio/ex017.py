from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print(f'O comprimento da hipotenusa do triângulo é {hip:.2f}.')
