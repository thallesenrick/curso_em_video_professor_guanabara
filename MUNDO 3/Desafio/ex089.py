alunos = []
print('.' * 30)
print(f'{"ESCOLA DE ARTES MICHELÂNGELO":^30}')
print('.' * 30)
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    alunos.append([nome, nota_1, nota_2, media])
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'N':
        break
print('.' * 30)
print(f'{"No.":<5}{"NOME":<15}{"MÉDIA":>5}')
print('.' * 30)
for c in range(0, len(alunos)):
    if alunos[c][3] < 7:
        print(f'\033[91m{c:<5}{alunos[c][0]:<15}{alunos[c][3]:>5.1f}')
    elif alunos[c][3] >= 7:
        print(f'\033[92m{c:<5}{alunos[c][0]:<15}{alunos[c][3]:>5.1f}')
print(f'\033[m{"." * 30}')
while True:
    quest = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if quest == 999:
        break
    else:
        print(f'\033[93mNotas de {alunos[quest][0]} são [{alunos[quest][1]}, {alunos[quest][2]}]')
        print(f'\033[m{"." * 30}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
print('.' * 30)
