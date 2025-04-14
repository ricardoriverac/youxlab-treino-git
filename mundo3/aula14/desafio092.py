pessoa = {}
pessoa['Nome'] = str(input('Nome: ')).capitalize().strip()
dataNascimento = int(input('Digite o ano de nascimento: '))
idade = 2025 - dataNascimento
pessoa['Idade'] = idade
pessoa['Gênero'] = str(input('Digite o gênero (F/M): ')).upper().strip()
pessoa['CTPS'] = str(input('N° da Carteira de Trabalho (Digite "0" se não possuir): ')).strip()

if pessoa['CTPS'] != '0':
    anoContratacao = int(input('Digite o ano da primeira contratação: '))
    if pessoa['Gênero'] == 'F':
        aposentadoria = (anoContratacao + 30) - dataNascimento
    else:
        aposentadoria = (anoContratacao + 35) - dataNascimento
    pessoa['Aposentadoria'] = aposentadoria

print('\n=== INFORMAÇÕES DA PESSOA ===')
for chave, valor in pessoa.items():
    print(f'O valor de {chave} é: {valor}')
