# cont = 1
# while cont <= 10:
#     print(cont, " -> ", end="")
#     cont += 1
# print("Acabou")


# numero = 0
# while numero != 999:
#     numero = int(input("Digite um numero: ")) 



# numero = contador = 0
# while contador < 10:
#     num = int(input("Digite um numero: "))
#     contador += 1

numero = soma = 0
while True:
    numero= int(input("Digite um numero"))
    if numero == 999:
       break
    soma += numero
print(f"[A soma  vale {soma}]")
        