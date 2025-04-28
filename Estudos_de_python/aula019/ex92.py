from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
dados['ano'] = int(input('Ano de nascimento: '))
dados['idade']= datetime.now().year - dados['ano']
dados['cpf'] = int(input('Digite seu cpf: '))

print( )
print('------DADOS DO CADASTRADO------')
print( )

if dados['cpf'] == 0:
    print(f'O nome dele e: {dados["nome"]} ')

    print(f'A idade dele e {dados["idade"]} ')

elif dados['cpf'] != 0:
    dados['contratacao'] = int(input('Em qual ano foi contratado: ')) 

    dados['salario'] = int(input('Qual seu salário: '))

    aposentadoria = (dados['contratacao'] + 40) - datetime.now().year 


    print(f'O nome dele e: {dados["nome"]} ')

    print(f'A idade dele e {dados["idade"]} ')

    print(f'Seu salário e: {dados["salario"]}')

    if aposentadoria >= 40:
        aposentadoria - 40
        print(f'Parabéns você ja esta aposentado faz {aposentadoria}')

    if aposentadoria < 40:
        aposentadoria - 40
        print(f'Ainda faltam {aposentadoria} anos para você se aposentar ')





