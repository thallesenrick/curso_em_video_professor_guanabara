from datetime import date
dados = dict()
dados['Nome'] = str(input('Digite seu nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nasc
dados['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] - nasc) + 35
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
