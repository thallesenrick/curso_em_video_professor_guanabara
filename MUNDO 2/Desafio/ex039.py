from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
sexo = str(input('Qual seu sexo? [m]asc ou [f}em: '))
if sexo == 'f':
    print('Não é obrigatório o alistamento!')
    print('Deseja continuar? [s]im ou [n]ão: ')
else:
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
    if idade < 18:
        saldo = 18 - idade
        print('Você AINDA NÃO tem idade de se alistar!')
        print(f'FALTAM ainda {saldo} anos!')
        ano_2 = atual + saldo
        print(f'Seu alistamento será em {ano_2}.')
    elif idade == 18:
        print('Está na HORA de se alistar!')
    elif idade > 18:
        saldo = idade - 18
        print('Você PASSOU do tempo de se alistar!')
        print(f'Você ULTRAPASSOU {saldo} anos!')
        ano_2 = atual - saldo
        print(f'Seu alistamento foi em {ano_2}.')
