# Solicita um número ao usuário
numero = int(input("Digite um número inteiro: "))
print('1.Binario \n 2.octal \n 3.hexadecimal')
escolha = int(input('Em qual você quer transformar?'))
binario = bin(numero)[2:]
octal = oct(numero) [2:]
hexa = hex(numero) [2:]

if escolha == 1:
    print(binario)
if escolha == 2:
    print(octal)
if escolha == 3:
    print(hexa)







# Converte para binário usando bin() e remove o prefixo '0b'
#binario = bin(numero)[2:]


# Exibe o resultado
#print(f"O número {numero} em binário é: {binario}")