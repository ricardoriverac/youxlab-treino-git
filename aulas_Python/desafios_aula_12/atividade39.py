print('\033[0;32m-==-==-==-Alistamento para o Serviço Militar-==-==-==-\033[m')
idade = int(input('Qual seu ano de nascimento? '))

#variaveis abaixo:

sub = 2025 - idade
tempof = 18 - sub
tempop = sub -18


if sub < 18:
    print('Você ainda tem que se alistar, faltam {} anos'.format(tempof))
    
elif sub == 18:
    print('Esse ano você tera que se alistar!!')
    
elif sub > 18:
    print('Seu tempo para se alistar ja passou! ({} anos atrás!)'.format(tempop))