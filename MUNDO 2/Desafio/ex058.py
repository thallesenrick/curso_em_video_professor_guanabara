from random import randint
pc = randint(0, 10)
contador = 1
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
jogador = int(input('Qual é o seu palpite? '))
while jogador != pc:
    if jogador > pc:
        print('\033[91mMenos... Tente mais uma vez.\033[m')
        jogador = int(input('Qual é o seu palpite? '))
        contador += 1
    elif jogador < pc:
        print('\033[94mMais... Tente mais uma vez.\033[m')
        jogador = int(input('Qual é o seu palpite? '))
        contador += 1
print(f'\033[93mAcertou com {contador} tentativas. Parabéns!\033[m')
