real = float(input('Quanto dinheiro você quer converter? '))
dolar = real / 5.26
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))