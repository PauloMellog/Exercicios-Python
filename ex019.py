import random

pa = input('Nome do primeiro da fila: ')
sa = input('Nome do segundo da fila: ')
ta = input('Nome do terceiro da fla: ')
lista = [pa, sa, ta]
escolhido = random.choice(lista)

print('O nome escolhido foi {}'.format(escolhido))

