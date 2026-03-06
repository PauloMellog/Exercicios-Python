#Calcular a média simples de um estudante.

print('Média de notas')

nota1 = float(input('Quanto foi sua primeira nota? '))
nota2 = float(input('Quanto foi sua segunda nota? '))
md = (nota1+nota2)/2
print('A média entre {} e {} é igual a {:.1f}.'.format(nota1, nota2, md))