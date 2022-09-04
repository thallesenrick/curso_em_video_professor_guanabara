from datetime import date
ano_atual = date.today().year
cont = 0
cont_2 = 0
for c in range(1, 8):
    idade = int(input('\033[93m'f'Em que ano a {c}ª pessoa nasceu? '))
    if ano_atual - idade >= 21:
        cont += 1
    elif ano_atual - idade <= 21:
        cont_2 += 1
print('\033[34m'f'Ao todo tivemos {cont} pessoas maiores de idade!')
print('\033[31m'f'E também tivemos {cont_2} pessoas menores de idade!')
