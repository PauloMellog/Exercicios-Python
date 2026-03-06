l = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))
area = l * h
print('Sua parede tem a dimensão de {:.2f} x {:.2f} com área de {:.2f}m²'.format(l, h, area))
print('Para pintar a parede será necessário {:.2f}l de tinta'.format(area/2))
