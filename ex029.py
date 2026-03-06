vel = float(input('Quantos km o carro passou o pardal: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado! Deverá pagar R${:.2f}!'.format(multa))
print('Tudo nas normalidades.')