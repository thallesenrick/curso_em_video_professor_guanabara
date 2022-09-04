velocidade = float(input('Qual é multi velocidade atual do carro? '))
multa = 7 * (velocidade - 80)

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Diriga com segurança!')
