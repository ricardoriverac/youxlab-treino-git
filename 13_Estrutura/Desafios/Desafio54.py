from datetime import date 
maior= 0
menor= 0

atual = date.today().year
for anos in range(1,8):
    nascimento=int(input("Digite ano do nascimento: "))
    idade= atual - nascimento

    if idade >= 18:
        maior += 1

    elif idade <= 0:
        print("\nEssa pessoa ainda nao nasceu.")
    else:
        menor += 1
print(f"Pessoas maiores de idade: {maior}")
print(f"Pessoas menores de idade: {menor}\n")


