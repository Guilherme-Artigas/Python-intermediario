nome = str(input('Qual é o seu nome: '))

if nome == 'Guilherme':
    print('Nome Show!')
elif nome == 'Juca' or nome == 'Salomé' or nome == 'Cintia':
    print('Nome maneiro!')
else:
    print('Seu nome e féio!')

print('Tenha um bom dia, {}'.format(nome))
