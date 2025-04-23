# exercicio proposto pelo rodrigao
from datetime import date
atual = date.today().year
trabalhador = {
    'nome':  str(input('Nome: ')),
    'sexo': str(input('Sexo [M/F] ')).upper(),
    'idade': int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de trabalho (0 não tem): ')) 
}
print(trabalhador)
if trabalhador['ctps'] == 0:
    for k , v in trabalhador.items():
        print(f'{k} tem o valor {v}')
else:
        trabalhador['salario'] = float(input('Salarío: '))
        trabalhador['contratação'] = int(input('Ano da contratação: '))
        idades = atual - trabalhador['idade']
        tempotrabalho = atual - trabalhador['contratação']
        if idades >= 65 and tempotrabalho >= 20 and trabalhador['sexo'] == 'M':
            print('Você Homem já pode se aposentar')
        elif idades >= 62 and tempotrabalho >= 15 and trabalhador['sexo'] == 'F':
            print('Você mulher já pode se aposentar')
        else:
            print('Voce nao esta apto a aposentar!')
