sidade=0
midadee=0
maiorid=0
nvelho=0
mulher20=0
for p in range (1 , 5):
    print('=-='* 20)
    print('Pessoa {} '.format(p))
    nome=str(input("Seu nome:  ")).strip()
    idade=int(input('Sua idade: '))
    gen=str(input('Qual seu gênero [F/M]: ')).strip()
    sidade += idade
    if p == 1 and gen in 'Mm':
        maiorid = idade
        nvelho =nome
    if gen in 'Mm' and idade > maiorid:
        maiorid =  idade
        nvelho = nome
    if gen in 'Ff' and  idade <20:
        mulher20 += 1
midadee  =sidade/4 
print('A media de idade do grupo e {}'.format(midadee))
print('O homem mais velho é {} é seu nome {}'.format(maiorid , nvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))