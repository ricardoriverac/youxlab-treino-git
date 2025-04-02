#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai
#parar quando o usuario digitar o valor 999, que a condição de parada. No final
#mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)

soma = 0
contador = True

while contador:
    n = int(input("Digite um número: "))

    if n == 999:
        print(f"A soma de todos números são : {soma}")
        break
    else:
        soma = soma + n
        
