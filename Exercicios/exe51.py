#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final
#mostre os 10 primeiros termos dessa progressão.

#Não sei, não lembro PA, CHAT GPT puro.
#Não sei nem oque e razao e termo.

primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")
for i in range(10):
    termo = primeiroTermo + i * razao
    print(termo, end=' ')
