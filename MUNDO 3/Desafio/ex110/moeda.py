def aumentar(n=0, p=0, formato=False):
    """
    --> FUNÇÃO DA ADIÇÃO (%):
    :param n: \033[1;33mValor multi ser declarado;\033[m
    :param p: \033[1;92mPorcentagem para aumentar;\033[m
    :param formato: \033[1;33mPara mostrar o valor na representação formatada ou não;\033[m
    :return: \033[1;33mMostra o valor de acordo com o parâmetro format escolhido;\033[m
    """
    res = n + (n * p / 100)
    return res if formato is False else moeda(n)


def diminuir(n=0, p=0, formato=False):
    """
    --> FUNÇÃO DA SUBTRAÇÃO (%):
    :param n: \033[1;33mValor multi ser declarado;\033[m
    :param p: \033[1;91mPorcentagem para diminuir;\033[m
    :param formato: \033[1;33mPara mostrar o valor na representação formatada ou não;\033[m
    :return: \033[1;33mMostra o valor de acordo com o parâmetro format escolhido;\033[m
    """
    res = n - (n * p / 100)
    return res if formato is False else moeda(n)


def dobro(n=0, formato=False):
    """
    --> FUNÇÃO DOBRO (2x)
    :param n: \033[1;33mValor multi ser declarado;\033[m
    :param formato: \033[1;33mPara mostrar o valor na representação formatada ou não;\033[m
    :return: \033[1;33mMostra o valor de acordo com o parâmetro format escolhido;\033[m
    """
    res = n * 2
    return res if not formato else moeda(n)


def metade(n=0, formato=False):
    """
    -> FUNÇÃO METADE (1/2)
    :param n: \033[1;33mValor multi ser declarado;\033[m
    :param formato: \033[1;33mPara mostrar o valor na representação formatada ou não;\033[m
    :return: \033[1;33mMostra o valor de acordo com o parâmetro format escolhido;\033[m
    """
    res = n / 2
    return res if not formato else moeda(n)


def moeda(n=0, moed='R$'):
    """
    --> FUNÇÃO REPRESENTAÇÃO
    :param n: \033[1;33mValor multi ser declarado;\033[m
    :param moed: \033[1;33mSímbolo gráfico da representação da moeda brasileira;\033[m
    :return: \033[1;33mMostra o valor de acordo com o parâmetro escolhido;\033[m
    """
    return f'{moed}{n:>.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=5):
    """
    --> FUNÇÃO DE VALORES (RESUMIDA)
    :param n: \033[1;33mValor multi ser declarado;\033[m
    :param taxaa: \033[1;92mPorcentagem para aumentar;\033[m
    :param taxar: \033[1;91mPorcentagem para diminuir;\033[m
    :return: \033[1;33mMostra o valor de acordo com o parâmetro escolhido;\033[m
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro(n))}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print(f'{taxaa}% de aumento: \t{moeda(aumentar(n, taxaa))}')
    print(f'{taxar}% de redução: \t\t{moeda(diminuir(n, taxar))}')
    print('-' * 30)
