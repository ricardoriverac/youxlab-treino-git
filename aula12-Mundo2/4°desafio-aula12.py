#Alistamento
from datetime import date
dataAtual=date.today().year
nascimento=int(input('Escreva sua data de nascimento: '))
idade=dataAtual-nascimento
if idade==18:
    print(f'Você ja tem {idade} anos, se aliste Imediatamente')
elif idade<18:
    faltam=18-idade
    print(f'Você tem {idade} anos, faltam {faltam} anos para você se alistar')
elif idade>18:
    passou=idade-18
    print(f'Você tem {idade} anos, Já se passou {passou} anos do seu alistamento, VOCÊ PRECISA PAGAR UMA MULTA')
