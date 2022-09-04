"""
Funções (Parte 2)
Parte Teórica
    -> Interactive Help (Ajuda interativa):
        - Abre o Python Console na barra inferior;
        - O comando utilizado é: help() e em seguida digita o que quer;
        - Pode ser escrito assim: help(print);
        - Ou assim: print(input.__doc__);

    -> Docstrings (Strings de documentação):
        - São os manuais escritos apos o comando def com (três aspas duplas);
        - Ver situação na linha 29;

    -> Parâmetro Opcional:
        - Ver situação na linha 47;

    -> Escopo de variáveis:
        - Variáveis globais ou escopo global:
            - Funcionam em toda extensão do código;
        - Variáveis locais ou escopo local:
            - Se estiver declarado em uma função, só funcionará na função;
        - Ver situação na linha 65;

    -> Retorno de resultados (return)
        - Ver situação na linha 80;
"""


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)


def somar(a2=0, b=0, c=0):
    """
    -> Faz multi soma de três valores e mostra o resultado na tela.
    :param a2: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    Função criada por Thalles Enrick durante as aulas do CursoemVideo
    """
    s = a2 + b + c
    print(f'A soma vale {s}.')


help(somar)
somar(3, 2, 5)
somar(8, 4)
somar()


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def somar(a1=0, b=0, c=0):
    """
    -> Faz multi soma de três valores e mostra o resultado na tela.
    :param a1: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    Função criada por Thalles Enrick durante as aulas do CursoemVideo
    """
    s = a1 + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Parte Prática


def fatorial(num1=1):
    f = 1
    for c in range(num1, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é Par')
