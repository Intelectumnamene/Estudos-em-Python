from datetime import datetime

aniversario = datetime(2024,3,21)
dias_para_aniversario = aniversario - datetime.now()
print(dias_para_aniversario)