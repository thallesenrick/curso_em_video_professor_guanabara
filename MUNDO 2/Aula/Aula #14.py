# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim')

n = 1
c_p = c_i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            c_p += 1
        else:
            c_i += 1
print(f'Você digitou {c_p} números pares e {c_i} números impares.')