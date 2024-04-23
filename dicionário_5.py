favorite_languages = {'jen': 'python', 'sarah': 'c'
                      , 'edward': 'ruby', 'phil': 'python', }
for nome, linguagem in favorite_languages.items():
    print("\n{} sua linguagem favorita é : {}"
          .format(nome.title(), linguagem.title()))