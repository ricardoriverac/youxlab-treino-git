#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
#Em um dicionario se por acaso a CTPS for diferente de ZERO, o dicionario recebera tambem o ano de contratação
# e o salario. Calcule e acrescente alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()
dados["nome"] = input("Digite o nome: ")
nascimento = int(input("Ano de nascimento: "))
dados["idade"] = datetime.now().year - nascimento

resposta = input("\nCarteira de Trabalho [S/N]: ").strip().upper()

if resposta not in ["S", "N"]:
    print(f"\nResposta inválida {dados['nome']}.")
    print("Programa finalizado.\n")
    exit()

dados["ctps"] = resposta

if resposta == "N":
    print(f"\nPrograma finalizado {dados['nome']}.\n")
    exit()

if resposta == "S":
    dados["ctps"] = "Sim"

dados["contratação"] = int(input("\nAno de contratação: "))
dados["salario"] = float(input("Salario R$: "))
dados["aposentadoria"] = dados["idade"] + ((dados["contratação"] + 35) - datetime.now().year)

print("\n")
for k, v in dados.items():
    if k == "idade":
        print(f"   - Idade: {v} anos")
    elif k == "aposentadoria":
        print(f"   - Vai se aposentar com: {v} anos de idade")
    elif k == "salario":
        print(f"   - Salario: R$ {v:.2f}")
    elif k == "contratação":
        print(f"   - Ano de contratação: {v}")
    elif k == "ctps":
        print(f"   - Possui carteira de trabalho: {v}")
    elif k == "nome":
        print(f"   - Nome: {v}")