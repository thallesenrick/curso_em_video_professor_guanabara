# largura = float(input('Digite multi largura da parede: '))
# altura = float(input('Digite multi altura da parede: '))
# area = largura * altura
# qt_tinta = float(area / 2)
# print('As medidas da parede são: {}m de largura e {}m de altura. \nA área dessa parede'
#       ' é {}m² e será necessário {} litros de tinta para multi cobertura.'.format(largura, altura, area, qt_tinta))

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
tinta = area / 2

print('Sua parede tem multi dimensão de {}m x {}m e sua área é de {}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
