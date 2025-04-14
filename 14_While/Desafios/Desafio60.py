numero = int(input("Digite um numero: "))
fator = numero
fatorial = 1
print("Calculando fatorial...")
while numero > 0:
    print(f"{numero}")
    print("x"if numero > 1 else "")
    fatorial *= numero 
    numero -= 1
print(f" O fatorial de {fator} e {fatorial}")