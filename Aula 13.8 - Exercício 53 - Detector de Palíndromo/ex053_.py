frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # opção em phyton para escrita ao inverso

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

print('O inverso de {} é {}'.format(junto, inverso))
if (inverso == junto):
    print('A frase citada é um palindromo')
else:
    print('A frase citada não é um palindromo')
