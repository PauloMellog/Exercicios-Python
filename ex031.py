dist = float(input('Quantos KM será sua viagem? '))
curta = dist * 0.5
longa = dist * 0.45
if dist < 200:
    print('Sua viagem custará R${} '.format(curta))
else:
    print('Sua viagem é longa, custará R${} '.format(longa))