print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if abs(b - c) < a < (b + c):
    print('Os seguimentos acima PODEM formar um triângulo!')
elif abs(a - c) < b < (a + c):
    print('Os seguimentos acima PODEM formar um triângulo!')
elif abs(a - b) < c < (a + b):
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo!')

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo!')
