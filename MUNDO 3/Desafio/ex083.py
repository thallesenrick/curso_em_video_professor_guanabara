# r = str(input('Digite uma expressão matemática: '))
# pilha = []
# for simb in r:
#     if simb == '(':
#         pilha.append('(')
#     elif simb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão está errada!')

n = str(input('Digite uma expressão matemática: '))
cont = 0
for simb in n:
    if simb == '(':
        cont += 1
    elif simb == ')':
        cont -= 1
if cont == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')