L = int(input('Digite o limite da sequencia de FIBONACCI: '))

c = 0
f1 = 0
f2 = 1
f3 = 0
print(f1, f2, end=' ')
while c <= L-3:
    f3 = f1 + f2
    print(f3, end=' ')
    f1 = f2
    f2 = f3
    c += 1
print('- FIM!')
