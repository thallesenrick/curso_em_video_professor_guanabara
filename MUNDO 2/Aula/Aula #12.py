# CONDIÇÕES ANINHADAS

nome = str(input('Qual é seu nome? '))
if nome == 'Thalles':
    print('Que nome bonito!')
elif nome == 'Enrick' or nome == 'André' or nome == 'Maciel':
    print('Seu nome é bem incomum no Brasil!')
elif nome in 'Francisco Sergio Luiz Carlos':
    print('É um nome masculino!')
elif nome in 'Ana Joana Catrina Luana':
    print('É um nome feminino!')
print(f'Tenha umm bom dia {nome}!')
