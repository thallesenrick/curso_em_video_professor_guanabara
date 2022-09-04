# EDIÇÃO DE DICIONÁRIOS
# Na hora de declarar usa-se chaves "{ }":
pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
# Na hora de referenciar usa-se colchete "[ ]":
print(f"O {pessoas['Nome']} tem {pessoas['Idade']} anos.")

# Para trocar uma variável por outra:
pessoas['Nome'] = 'Leandro'
# Para adicionar uma key (Não necessita de ".append"):
pessoas['Peso'] = 98.50
# Para excluir uma key: "del pessoas['Sexo']"

# Para printar as chaves / categorias: print(pessoas.keys())
for k in pessoas.keys():
    print(k)
# Para printar os valores que foram atribuidos as keys: print(pessoas.values())
for v in pessoas.values():
    print(v)
# Para printar em conjunto: print(pessoas.items())
for i in pessoas.items():
    print(i)
# Usando duas variáveis (For Keys, Values in items):
for k, v in pessoas.items():
    print(f'{k} = {v}')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# DICIONÁRIOS DENTRO DE LISTAS
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'SIGLA': 'RJ'}
estado2 = {'UF': 'São Paulo', 'SIGLA': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
# Criou-se uma lista com dois dicionários dentro [ {} {} ]
# (brasil[0]['UF']) = "Rio de Janeiro"
# (brasil[1]['SIGLA'] = "SP"
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# FAZER COPIAS DE DICIONÁRIOS PARA LISTA
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['SIGLA'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:  # For da Lista (Para cada estado in Brasil)
    for v in e.values():  # For do dicionário (valor em 'e')
        print(v, end=' ')
    print()
