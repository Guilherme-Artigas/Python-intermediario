valor = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu salário: '))
x = int(input('Quantos anos você pretende pagar: '))

prestacao = valor / (12 * x)
trinta = salario * 30 / 100

if prestacao < trinta:
    print('Parabens o emprestimo foi aprovado!')
    print('Pagamentos no valor de R${:.2f}, em {} vezes!'.format(prestacao, 12 * x))
else:
    print('Infelizmente o emprestimo nao foi aprovado! o valor da mensalidade é maior do que 30% do seu salário.')
