lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar....')
    r = str(input('Quer continuar? [ S / N ] ')).upper()
    if r in 'N':
        break
print('-=-' * 20)
print(f'Você digitou os valores {sorted(lista)}')