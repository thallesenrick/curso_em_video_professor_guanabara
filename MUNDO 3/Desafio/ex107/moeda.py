def aumentar(n, p):
    res = n + (n * p / 100)
    return res


def diminuir(n, p):
    res = n - (n * p / 100)
    return res


def dobro(n):
    res = n * 2
    return res


def metade(n):
    res = n / 2
    return res


def moeda(n):
    res = f'R${n:.2f}'
    return res