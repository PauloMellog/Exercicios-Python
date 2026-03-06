#Sistema simples de aluguel de carros
#Custa R$60 por dia e R$ 0,15 por km rodado.

km = float(input('Quantos km foram rodados: '))
dias = float(input('Quantos dias se passaram com o veículo: '))
preco = (km * 0.15) + (dias * 60)

print('O valor total a se pagar é de R${:.2f}'.format(preco))