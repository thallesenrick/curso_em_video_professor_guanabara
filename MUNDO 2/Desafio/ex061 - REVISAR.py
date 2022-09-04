print('=-=' * 10)
print('{:^30}'.format('Termos de um PA'))
print('=-=' * 10)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite multi razão: '))
cont = 1
termo = p
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont += 1
print('FIM')