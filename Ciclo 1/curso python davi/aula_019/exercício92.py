from datetime import datetime
pessoa = {}
pessoa['nome'] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['ctps'] = int(input("Carteira de trabalho (0 se não tem): "))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input("Ano de contratação: "))
    pessoa['salário'] = float(input("Salário: R$ "))
    tempo_contribuicao = 35
    pessoa['aposentadoria'] = (pessoa['contratação'] + tempo_contribuicao) - nascimento
print("Dados cadastrados:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")