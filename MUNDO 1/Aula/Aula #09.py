"""
Manipulando Strings
frase = 'Curso em Vídeo Python'

FATIAMENTO - 'O ultimo valor não entra na contagem'
print(frase[9]) - 'Aqui ele pega apenas o índice selecionado.'
print(frase[9:14]) - 'Aqui ele pega entre o 9 e 13.'
print(frase[9:21]) - 'Aqui ele pega até o final pois acaba no índice 20.'
print(frase[9:21:2]) - 'O ultimo 2 refere-se multi ir pulando de 2 em 2.'
print(frase[:5]) - 'Aqui ele começa do 0 e vai até o 5.'
print(frase[15:]) - 'Aqui ele começa no 15 e vai até o fim da string'
print(frase[9::3]) - 'Começa no 9, vai até o fim, pulando de 3 em 3.'

ANÁLISE
print(len(frase)) - 'Mostra o comprimento. EX: 21'
print(frase.count('o')) - 'Mostra quantas vezes existe o cacartere. Sempre usar ('')'
print(frase.count('o', 0, 13)) - 'Considera do 0 até o 12, e conta quantos 'o' tem.'
print(frase.find('deo')) - 'Mostra em que momento começou. EX: 11'
print(frase.find('Android')) - 'Se nao existe retorna -1.'
print('Curso' in frase) - 'Existe 'Curso' em frase? True.'

TRANSFORMAÇÃO
print(frase.replace('Python', 'Android')) - 'Substitui uma  palavra por outra'
print(frase.replace('o', '!')) - 'Substitui um caracter por outro também.'
print(frase.upper()) - 'Em maiúsculo'
print(frase.lower()) - 'Em minúsculo'
print(frase.title()) - 'Primeira letra em maiúsculo.'
print(frase.capitalize()) - 'Deixa apenas o primeiro caractere minúsculo.'
frase = '   Aprenda Python  '
print(frase.strip()) - 'Remove espaços vazios no começo e fim da string.'
print(frase.rstrip()) - 'Remove espaços da direita'
print(frase.lstrip()) - 'Remove espaços da esquerda'

DIVISÃO
print(frase.split()) - 'Ele pega onde tem espaço e cria uma divisão em uma lista'

JUNÇÃO
frase_2 = 'Meu amigo da escola é um macaco'
separada = frase_2.split()
print(' '.join(separada))
"""

# frase = 'Curso em Vídeo Python'
# dividido = frase.split()
# print(dividido [2] [2])
