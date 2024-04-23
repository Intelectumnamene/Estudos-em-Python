from datetime import datetime
import random
nome = input('Qual seu nome?')
idade = int(input('Qual sua idade? '))
data_de_registro = datetime.now()
print(data_de_registro)
print('Olá {} obrigado pelo cadastro você receberá um cartão de '.format(nome))
sorteio = ['R$50','R$250', 'R$120']
cartao = print(random.choice(sorteio))




