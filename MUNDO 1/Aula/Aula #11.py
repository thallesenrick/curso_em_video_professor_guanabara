"""
\033[0;33;44m

1º ESTILO (EX: 0)   |    2º TEXTO (EX: 33)    |     3º FUNDO (EX: 44)
0 - NORMAL          |    30 - PRETO           |     40 - PRETO
1 - NEGRITO         |    31 - VERMELHO ESCURO |     41 - VERMELHO ESCURO
4 -SUBLINHADO       |    32 - VERDE           |     42 - VERDE
7 - NEGATIVO        |    33 - AMARELO         |     43 - AMARELO
                    |    34 - AZUL            |     44 - AZUL
                    |    35 - MAGENTA         |     45 - MAGENTA
                    |    36 - CIANO           |     46 - CIANO
                    |    37 - CINZA CLARO     |     47 - CINZA CLARO
                    |    90 - CINZA ESCURO    |    100 - CINZA ESCURO
                    |    97 - BRANCO          |    107 - BRANCO
"""

# print('{}Teste{}'.format('\033[0;30;41m', '\033[m'))
# print('{}Teste{}'.format('\033[4;33;46m', '\033[m'))
# print('{}Teste{}'.format('\033[1;35;43m', '\033[m'))
# print('{}Teste{}'.format('\033[30;42m', '\033[m'))
# print('{}Teste{}'.format('\033[m', '\033[m'))
# print('{}Teste{}'.format('\033[7;30m', '\033[m'))

# multi = 3
# b = 5
# print(f'Os valores são \033[92m{multi}\033[m e \033[31m{b}\033[m!!!')

# nome = input('Digite seu nome: ')
# cores = {'limpa': '\033[m',
#          'azul': '\033[34m',
#          'amarelo': '\033[33m',
#          'pretoebranco': '\033[7;97m'}
#
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
# print(f'Olá! Muito prazer em te conhecer, \033[4;34m{nome}\033[m!!!')
