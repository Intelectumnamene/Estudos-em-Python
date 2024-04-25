prompt = "\nEntre com uma cidade a qual você já visitou:"
prompt += "\n Ou digite 'quit para encerrar o programa'"
while True:
    cidade = input(prompt)
    if cidade == 'quit':
        break
    else:
        print("Eu amo ir para : {}".format(cidade.title()))