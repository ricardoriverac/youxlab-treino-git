from datetime import datetime


ano_atual = datetime.now().year


pessoa = {}


pessoa['nome'] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
pessoa['idade'] = ano_atual - nascimento
pessoa['ctps'] = int(input("carteira de trabalho (0 se não tiver): "))


if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input("Ano deee contratação: "))
    pessoa['salario'] = float(input("Salário: R$"))
  
    anos_contribuicao = 35
    pessoa['aposentadoria'] = (pessoa['contrreatacao'] + anos_contribuicao) - nascimento


print("\nDados cadastrados:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
