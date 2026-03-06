nome = str(input('Iforme seu nome completo: ')).strip()
dividido = str(nome.split())

print('Tem Silva no nome? {}'.format('SILVA' in dividido.upper()))