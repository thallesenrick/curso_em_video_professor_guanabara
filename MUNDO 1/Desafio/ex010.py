# carteira = float(input('Digite o valor em sua carteira: R$'))
# print(f'Você poderá comprar ${carteira/5.10:.2f} dólares.')

real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = real / 5.10
euro = real / 5.69
yen = real / 0.044
libra = real / 6.82

print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}.'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥{:.2f}.'.format(real, yen))
print('Com R${:.2f} você pode comprar £{:.2f}.'.format(real, libra))
