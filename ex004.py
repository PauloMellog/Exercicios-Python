#Alfanumérico ou numérico?

entrada_usuario = input('Digite algo: ')
print('{} é um número?'.format(entrada_usuario), entrada_usuario.isnumeric())
print('{} é um caractere alpha?'.format(entrada_usuario), entrada_usuario.isalpha())