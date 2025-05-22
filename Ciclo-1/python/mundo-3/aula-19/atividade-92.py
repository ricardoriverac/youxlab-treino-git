from datetime import datetime

ano_atual = datetime.now().year

# Cadastro da pessoa
cadastro = {}

cadastro['nome'] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
cadastro['idade'] = ano_atual - nascimento
cadastro['ctps'] = int(input("Número da CTPS (0 se não tiver): "))

if cadastro['ctps'] != 0:
    cadastro['ano_contratacao'] = int(input("Ano de contratação: "))
    cadastro['salario'] = float(input("Salário: R$ "))
    # Calculando idade de aposentadoria (35 anos de contribuição)
    anos_contribuicao = 35
    idade_aposentadoria = (cadastro['ano_contratacao'] + anos_contribuicao) - nascimento
    cadastro['idade_aposentadoria'] = idade_aposentadoria

# Mostrando o resultado
print("\n--- DADOS CADASTRADOS ---")
for chave, valor in cadastro.items():
    print(f"{chave.capitalize()}: {valor}")
