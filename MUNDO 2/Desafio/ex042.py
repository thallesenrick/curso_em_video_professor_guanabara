print('-=-' * 9)
print('CALCULADORA DE TRIÂNGULOS')
print('-=-' * 9)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima PODEM formar um triângulo!')
    if a == b == c:
        print('É um triângulo equilátero!')
    elif a == b or b == c or a == c:
        print('É um triângulo isóceles!')
    else:
        print('É um triângulo escaleno!')
else:
    print('Não pode formar um triângulo!')


