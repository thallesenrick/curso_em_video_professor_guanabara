n = soma = contador = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        contador += 1
print(f'Você digitou {contador} números e a soma entre eles foi de {soma}.')

m = s = c = 0
m = int(input('Digite um número [999 para parar]: '))
while m != 999:
    s += m
    c += 1
    m = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {c} números e a soma entre eles foi de {s}.')