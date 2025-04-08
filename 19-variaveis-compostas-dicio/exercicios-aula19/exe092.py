from datetime import date
atual = date.today().year
anosparaaposentar = 35
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
    trabalhador['contração'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salario: '))
    aposentaria = anosparaaposentar + trabalhador['contração'] - trabalhador['idade']
    for k , v in trabalhador.items():
        print(f'{k} tem o valor {v}')
    print(f'Você ira se aposentar com {aposentaria}')