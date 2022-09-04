from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade <= 14:
    print('Sua categoria é INFANTIL!')
elif idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade <= 25:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
