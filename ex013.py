#Trabalhando com porcentagem, aumento de valores

salario = float(input('Quanto ganha o funcionário? R$'))
aum = salario + (salario * 15/100)

print('O funcionário que recebia R${:.2f}, com 15% e aumento, receberá R${:.2f}'.format(salario, aum))