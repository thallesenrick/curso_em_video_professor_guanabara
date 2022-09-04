def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um Inteiro: ')
num2 = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {num2}.')