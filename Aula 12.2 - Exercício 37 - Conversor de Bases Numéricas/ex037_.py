n = int(input('Digite um número inteiro: '))

print()

print('Escolha uma das bases para conversão:')
print(' [ 1 ] Converte para BÍNARIO')
print(' [ 2 ] Converte para OCTAL')
print(' [ 3 ] Converte para HEXADECIMAL')

print()
opcao = int(input('ESCOLHA SUA OPÇÃO: '))

if (opcao >= 1) and (opcao <= 3):

    if opcao == 1:
        print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
    elif opcao == 2:
        print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
    elif opcao == 3:
        print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))

else:
    print('Valor digitado para conversão inexistente!')
