from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return 'NEGADO'
    if idade >= 100 :
        return 'OPCIONAL'
    if idade >= 18 and idade < 100:
        return 'OBRIGATORIO'

    

#programa principal

ano_de_nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano_de_nascimento
print(f'Você tem {idade} é seu voto serã: {voto(ano_de_nascimento)}')
