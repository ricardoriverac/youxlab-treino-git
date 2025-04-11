# exercicio proposto pelo rodrigao
from datetime import date
atual = date.today().year
trabalhador = {
    'nome':  str(input('NOME: ')),
    'idade': int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira de trabalho (0 não tem): ')) 
}
if trabalhador['ctps'] == 0:
    print(trabalhador)
    for k , v in trabalhador.items():
        print(f'{k} tem o valor {v}')
else:
    trabalhador['contratação'] = int(input('Ano da contratação: '))
    trabalhador['salario'] = float(input('Salarío: '))
    idades = atual - trabalhador['idade']
    tempotrabalho = atual - trabalhador['contratação']
    if idades >= 65 and tempotrabalho >= 20:
        print('Voce esta apto a aposentar')
    print('Voce nao esta apto a aposentar!')
