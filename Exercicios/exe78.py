#Faça um programa que leia 5 valores numericos e aguarde os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


tabelaDeNum = []

for _ in range(5):
    num = int(input("Digite um número: "))
    tabelaDeNum.append(num)

print(f"Os números da tupla são: {tabelaDeNum}")
print(f"O menor número da tabela é {min(tabelaDeNum)}")
print(f"O maior número da tabela é {max(tabelaDeNum)}")