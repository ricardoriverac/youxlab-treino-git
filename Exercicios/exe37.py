numero = int(input("Digite um número: "))
escolha = input("Qual você deseja: 1 - Binário, 2 - Octal, 3 - Hexadecimal? ").lower()

if escolha in ["1", "binário", "binario"]:
    print(f"O número {numero} em binário é: {bin(numero)[2:]}")
elif escolha in ["2", "octal"]:
    print(f"O número {numero} em octal é: {oct(numero)[2:]}")
elif escolha in ["3", "hexadecimal"]:
    print(f"O número {numero} em hexadecimal é: {hex(numero)[2:]}")
else:
    print("Erro: Escolha inválida!")
