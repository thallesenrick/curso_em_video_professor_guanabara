from time import sleep


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        print('ERRO! Digite um valor diferente de 0')
        c = int(input('Passo: '))
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}:')
    sleep(1)
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            cont += c
            sleep(0.3)
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            cont -= c
            sleep(0.3)
    print('FIM!')
    sleep(0.3)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar multi contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
print('-=' * 20)
