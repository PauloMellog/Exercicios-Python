#Porcentagem, desconto

val = float(input('Qual o valor do seu produto: R$'))
desc = val - (val*5/100)
print('O valor de R${:.2f} ficará R${:.2f} com o desconto de 5% aplicado.'.format(val, desc))