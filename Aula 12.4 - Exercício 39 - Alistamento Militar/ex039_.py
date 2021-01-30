from datetime import date

ano_atual = date.today().year

sexo = str(input('Digite seu Sexo [Homem / mulher]: '))

if (sexo == 'Homem') or (sexo == 'homem') or (sexo == 'H') or (sexo == 'h'):

    ano_N = int(input('Digite o ano do seu nascimento: '))

    idade = ano_atual - ano_N

    print()
    print('Quem nasceu em {} tem {} anos em {}'.format(ano_N, idade, ano_atual))
    print()

    if idade < 18:
        print('Você ainda não tem a idade suficiente para o alistamento militar obrigatório!')
        print('Sua idade: {} anos... faltam {} anos para o seu alistamento! que sera em {}'.format(idade, 18 - idade, (18 - idade) + ano_atual))
    elif idade > 18:
        print('Você ja passou da idade do alistamento militar obrigatório!')
        print('Sua idade: {} anos... ja se passaram {} anos do seu alistamento! que foi em {}'.format(idade, idade - 18, ano_atual - (idade - 18)))
    else:
        print('Sua idade: {} anos... você deve se alistar imediatamente!'.format(idade))

else:
    print('O alistamento militar é obrigatorio para homens! obrigado por responder tenha um bom dia...')

# Minha solução
'''
ano = int(input('Digite o ano do seu nascimento: '))
ano_a = int(input('Digite o ano atual: '))
idade = ano_a - ano

if idade < 18:
    print('Você ainda não tem idade paras se alistar!')
    print('Faltam {} anos para você ter a idade necessaria...'.format(18 - idade))
elif idade == 18:
    print('Você esta na idade de se apresentar para o alistamento!')
else:
    print('Você ja passou {} anos, da fase de alistamento!'.format(idade - 18))
'''
