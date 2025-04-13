primeiro= int(input("Primeiro numero: "))
segundo= int(input("Segundo numero: "))
opçao = 0
multiplicar = primeiro * segundo
maior = primeiro > segundo and segundo > primeiro
while opçao != "5":
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos numeros
[ 5 ] Sair do programa ''')
    opçao = str(input("Qual sua escolha: "))
    if opçao == "1":
        soma =  (primeiro + segundo)
        print(f"A soma de {primeiro} com {segundo} vai ficar {soma}")
    elif opçao == "2":
     print(f"A multiplicação de {primeiro} com {segundo} vai ficar {multiplicar}") 
    elif opçao == "3":
        print(f"Entre {primeiro} e {segundo} o maior e {maior}")
    elif opçao == "4":
        print("Informe os numeros novamente")
        primeiro = int(input("Primeiro valor: "))
        segundo = int(input("Segundo valor: "))
    elif opçao == "5":
        print("Finalizando...")  
    else:
        print("Dados invalidos!, tente novamente. ")
    print("======" * 4)
print("Fim do programa")

