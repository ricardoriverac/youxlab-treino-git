#Crie um programa que tenha uma função chamada voto() que vai receber como parametro
# O ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
# Negado, Opcional ou Obrigatorio nas eleições

from datetime import datetime

def cabecalho(texto):
    largura = len(texto) + 8
    print("~" * largura)
    print(f"{texto.center(largura)}")
    print("~" * largura)

def voto(idade):
    if idade > 100:
        print("Você está morto, não tem como votar... desculpa estou brincando. desejo saúdes.")
    if idade < 16:
        print("Voto negado (não pode votar)")
    elif 16 <= idade < 18 or idade >= 70:
        print("Voto opcional (facultativo)")
    else:
        print("Voto obrigatório")
    

cabecalho("Digite o seu nascimento:")

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

dataNasc = datetime(ano, mes, dia)
hoje = datetime.now()

idade = hoje.year - dataNasc.year
if (hoje.month, hoje.day) < (dataNasc.month, dataNasc.day):
    idade -= 1

print("\n")
cabecalho("Situação do voto:")

print("\n")
print(f"Sua idade é: {idade} anos")
print(f"Situação do voto: {voto(idade)}")
print("\n")
