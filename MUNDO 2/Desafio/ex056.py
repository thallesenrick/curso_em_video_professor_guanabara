soma_idade = 0
mais_velho = 0
nome_velho = ''
cont_sexo = 0
for c in range(1, 5):
    print(f'_____ {c}ª PESSOA _____')
    nome = str(input('Digite o Nome: '))
    idade = int(input('Digite multi Idade: '))
    sexo = str(input('Digite o Sexo [M/F]: '))
    soma_idade += idade
    media = soma_idade / 4
    if c == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        cont_sexo += 1
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_velho}.')
print(f'Ao todo são {cont_sexo} mulheres com menos de 20 anos.')
