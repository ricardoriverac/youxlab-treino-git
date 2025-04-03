#Desenvolva um programa que leia quatro valores pelo teclado e aguarde-os em uma tupla. No final, mostre
#Quantas vezes apareceu o valor 9
#Em que posição foi digitado o primeiro valor 3
#Quais foram os números pares

tabelaNum = ()

for n in range(4):
    num = int(input("Digite um valor: "))
    tabelaNum = tabelaNum + (num,) 

print(f"\nOs valores digitados foram: {tabelaNum}")

print(f"O valor 9 apareceu {tabelaNum.count(9)} vezes")

if 3 in tabelaNum:
    print(f"O primeiro valor 3 apareceu na {tabelaNum.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado.")

print("Os números pares digitados foram:", end=" ")
temPar = False 

for num in tabelaNum:
    if num % 2 == 0:
        print(num, end=" ")
        temPar = True

if not temPar:
    print("Nenhum")

