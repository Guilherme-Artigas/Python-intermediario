from time import sleep

controle = True
total = Produto = menor_preco = 0

print('*-' * 13)
print(' * LOJA SUPER BARATEZA * ')
print('*-' * 13)
print()

while controle == True:

    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))

    total += preco

    if preco > 1000:
        Produto += 1
    if menor_preco == 0 or preco < menor_preco: # Produto_B = Produto mais barato!
        menor_preco = preco
        Produto_B = nome

    controle2 = True
    while controle2 == True:
        resposta = str(input('Continuar [S/N]: ')).strip().upper()[0]
        if resposta == 'S':
            controle = True
            controle2 = False
        elif resposta == 'N':
            controle = False
            controle2 = False
        else:
            print(f'Você digitou uma opção invalida! Aguarde... ')
            sleep(3)
            controle2 = True
            print()
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'Total da compra: R$ {total:.2f} ')
print(f'Foram {Produto} produtos custando mais de R$ 1.000')
print(f'Item mais barato foi {Produto_B} custando R$ {menor_preco:.2f}')
