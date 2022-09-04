numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    pergunta = str(input('Deseja continuar? [ S / N ]: '))
    if pergunta in 'Ss':
        while True:
            n = int(input('Digite um número entre 0 e 20: '))
            if 0 <= n <= 20:
                break
            print('Tente novamente. ', end='')
        print(f'Você digitou o número {numero[n]}.')
    else:
        break
print('FIM!')