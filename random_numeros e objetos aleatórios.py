import random
print(random.random())#gerar valor de 0.0 a 1.0
print(random.randint(4, 10))#gerar  valor inteiro de valor mínimo ao valor máximo
print(random.uniform(4, 10))#gerar  valor decimal do valor mínimo ao valor máximo

cores = ['verde','vermelho', 'azul']
print(random.choice(cores))
print(random.choices(cores,k=2))

cartas_de_um_baralho = ['carta1','carta2','carta3','carta4']
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)

moeda = ['cara','coroa']
print(random.choice(moeda))

nomes = ["Ana", "Pedro", "Maria", "João", "Sofia"]
print(random.choice(nomes))

numeros = (10,100)
print(random.randint(*numeros))