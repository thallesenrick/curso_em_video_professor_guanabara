sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('INVALIDO! Por favor informe seu sexo: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo Masculino registrado!')
if sexo == 'F':
    print('Sexo Feminino registrado!')