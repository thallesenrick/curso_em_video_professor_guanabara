salario = float(input('Digite o salário do funcionário: '))
aumento = salario + (15/100 * salario)
print('O salário antigo de R${} passa multi ser R${}.'.format(salario, aumento))

salario_2 = float(input('Qual é o salário do funcionário? R$'))
novo = salario_2 + (salario_2 * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa multi receber R${:.2f}.'.format(salario_2, novo))
