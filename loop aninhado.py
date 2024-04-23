paises = ['Brasil', 'Índia', 'estados unidos']
estacoes_do_ano = ['primavera', 'verão', 'outono', 'inverno']
for pais in paises:
    for estacao in estacoes_do_ano:
        print(f'{pais} {estacao}')
        
for x in range(1,11):
    for y in range(1,6):
        print(f'Valor externo {x} e internode {y}')
    

celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']

versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'{celular} = {versao}' )