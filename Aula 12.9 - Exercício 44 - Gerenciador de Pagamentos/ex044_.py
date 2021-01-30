print('{:=^40}'.format(' Lojas Marijuanas '))

valor = float(input('Digite o valor da compra R$ '))

print()

print(' ************ Formas de Pagamento ************')
print(' 1 - Dinheiro/Cheque à vista: 10% de desconto.')
print(' 2 - Cartão à vista: 5% de desconto.')
print(' 3 - Em até 2x, valor total sem desconto.')
print(' 4 - 3x ou mais 20% de juros')
print(' *********************************************')

print()

opcao = int(input('Escolha a forma de pagamento [1, 2, 3, 4]: '))

print()

if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:

    if opcao == 1:
        valorF = valor - (valor * 10 / 100)
        print('Obrigado pela preferencia!')
        print('Valor final da sua compra: R$ {:.2f} á vista.'.format(valorF))
        print('Você ganhou um desconto de R$ {}'.format(valor * 10 / 100))
    elif opcao == 2:
        valorF = valor - (valor * 5 / 100)
        print('Obrigado pela preferencia!')
        print('Valor final da sua compra: R$ {:.2f} á vista no cartão'.format(valorF))
        print('Você ganhou um desconto de R$ {}'.format(valor * 5 / 100))
    elif opcao == 3:
        valorF = valor / 2
        print('Obrigado pela preferencia!')
        print('Valor final da sua compra: R$ {:.2f}... 2x de R$ {:.2f} sem desconto.'.format(valor, valorF))
    elif opcao == 4:
        valorF = valor + (valor * 20 / 100)
        parcelas = int(input('Escolha a quantidade de parcelas, entre [3 e 12x]: '))
        print()
        print('Obrigado pela preferencia!')
        print('Valor final da sua compra: R$ {:.2f} dividido em {}x de R$ {:.2f}'.format(valorF, parcelas, valorF / parcelas))

else:
    print('OPERAÇÃO CANCELADA, VOCÊ DIGITOU UMA OPÇÃO INVALIDA!')
