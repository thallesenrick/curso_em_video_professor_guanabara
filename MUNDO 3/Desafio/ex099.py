from time import sleep


def maior(* num):
    cont = maiorr = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ')
        sleep(0.3)
        if cont == 0:
            maiorr = c
        else:
            if c > maiorr:
                maiorr = c
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maiorr}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
