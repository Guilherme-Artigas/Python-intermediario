valor = int(input('Digite um valor para descobrir seu FATORIAL: '))

n1 = valor
c = valor - 1
fatorial = 1

while c >= 1:
    fatorial = valor * c
    valor = fatorial
    c -= 1
print()

print('{}! = {}'.format(n1, fatorial))
