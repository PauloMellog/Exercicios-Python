n = int(input('Digite seu número: '))
print('O dobro de {} vale {}. \n'
      'O triplo de {} vale {}. \n'
      'A raiz quadrada de {} vale {:.3f}.'
      .format(n, (n*2), n, (n*3), n, (n**(1/2)) ))