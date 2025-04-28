from datetime import datetime
lista = []
dados = {}
dados['Nome'] = str(input('nome: ')).title().strip()
anon = int(input('Digite o ano de nascimento : '))
dados['Idade'] = datetime.now().year - anon
carteira = int(input('Digite a carteira de trabalho (0 não tem): '))
if carteira != '0':
    dados['Ctps'] = carteira
    dados['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o Salário atual: '))
    dados['aposentadoria'] = dados['Idade'] + dados['Ano de Contratação'] + 35 - datetime.now().year
lista.append(dados.copy())
print('--'*40)
for k, v in dados.items():
    print(f'- {k} é {v}.')