# Funções ou def - parte 1
# PARTE TEÓRICA
# Funções estão ligadas ao ideal de "rotina (coisas que você faz constatemente)";
# Algumas funções ja utilizadas: print(), len(), input(), int(), float();
# As funções são escritas com "def xxxxx():" e na identenção é descrito multi função;
# Entre multi def e o programa principal tem que ter 2 linhas vazias;
# Exemplo:
# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)
# titulo('       CURSO EM VÍDEO       ')
# titulo('       APRENDA PYTHON       ')
# titulo('       THALLES ENRICK       ')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# PARTE PRÁTICA
# def soma(multi, b):
#     print(f'A = {multi} e B = {b}')
#     s = multi + b
#     print(f'A soma de A + B = {s}')
# soma(4, 5)
# # ou
# soma(b=4, multi=5), '''ou''', soma(multi=4, b=5)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# def contador(* num):
#     print(f'Recebi os valores {num} e são ao todo {len(num)} números.')
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
