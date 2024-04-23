from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

lancamento_app = datetime(2021,5,28)
print(lancamento_app)

data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo? '),'%d/%m/%Y')
print(type(data_de_lancamento))

data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)