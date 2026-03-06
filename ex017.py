from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hp = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hp))