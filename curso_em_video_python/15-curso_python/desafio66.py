numeros = 0
lista = [ ]
while True:
    numeros = int(input('Digite um número: '))
    print('\033[1;35mOBSERVAÇÂO \033[0;0m: o programa só vai parar quando digitar \033[1;33m999 \033[0;0m')
    lista.append(numeros)
    if numeros == 999:
        break
    soma = sum(lista)
    quantidade = len(lista)
print(f'A quantidade de números digitados foi {quantidade}')
print(f'A soma entre todos os números foi {soma}')