dados = dict()
lista = list()
soma = 0
while True:
    dados['nome'] = str(input('Digite seu nome: '))
    dados['sexo'] = str(input('Digite seu sexo: [M/F] ')).upper()
    if dados['sexo'] not in 'MF':
        print('ERRO! Responda apenas M ou F.')
        dados['sexo'] = str(input('Digite seu sexo: [M/F] ')).upper()
    dados['idade'] = int(input('Digite sua idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resposta = str(input('Quer continuar? [S/N] ')).upper()
    if resposta == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print(f'\nD) Lista das pessoas que estão acima da idade média:')
for p in lista:
    if p['idade'] > media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print('<< ENCERRADO >>')
