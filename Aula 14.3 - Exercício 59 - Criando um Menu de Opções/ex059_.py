r = 's'
while r == 's':
    n1 = int(input('Digite o 1º valor: '))
    n2 = int(input('Digite o 2º valor: '))

    print(' [ 1 ] SOMAR')
    print(' [ 2 ] Multiplicar')
    print(' [ 3 ] Maior')
    print(' [ 4 ] Novos Números')
    print(' [ 5 ] Sair do Programa')
    opcao = int(input('Escolha uma operação: '))

    if (opcao == 1):
        soma = n1 + n2
        print('Resultado da SOMA entre {} e {} = {}'.format(n1, n2, soma))
        r = 's'
    elif (opcao == 2):
        m = n1 * n2
        print('Resultado da MULTIPLICAÇÃO entre {} e {} = {}'.format(n1, n2, m))
        r = 's'
    elif (opcao == 3):
        if (n1 > n2):
            maior = n1
            print('Maior valor digitado entre {} e {} = {}'.format(n1, n2, maior))
            r = 's'
        elif (n2 > n1):
            maior = n2
            print('Maior valor digitado entre {} e {} = {}'.format(n1, n2, maior))
            r = 's'
    elif (opcao == 4):
        r = 's'
        print('Você escolheu digitar novos valores!')
    elif (opcao == 5):
        r = 'n'
        print('Finalizando Programa')
