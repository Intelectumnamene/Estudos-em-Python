frase1 = 'Desafio manipulação de strings'

frase2 = 'jhonatan,rafael,carol,camilla'

palavras1 = frase1.split()
palavras2 = frase2.split(',')
print(','.join(palavras1))
print(' & '.join(palavras2))
