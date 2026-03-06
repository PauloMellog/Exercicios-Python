import random
num = int(input('Qual número de 0 a 5 estou pensando? '))
n = [0,1,2,3,4,5]
correto = random.choice(n)
if num == correto:
    print('PARABÉNS, você acertou!')
else:
    print('Poxa, você errou! Era {}!'.format(correto))
