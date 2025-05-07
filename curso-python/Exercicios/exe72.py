#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
#Por extenso, de zero ate 20

#seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por exetenso

cont = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis",
        "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze",
        "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um número entre 0 a 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente.", end="")
print(f"Voce digitou o número {cont[num]}")