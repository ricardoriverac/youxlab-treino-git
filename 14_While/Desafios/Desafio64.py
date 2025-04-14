num = cont = soma = 0
while num != 999:
    num = int(input("Digite um numero [999] para parar: "))
    soma += num
    cont += 1
print(f"Voce digitou {cont-1}  numeros e a soma entre eles foi {soma -999}")