#Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns
#termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
quaTermo = int(input("Digite a quantidade de termos: "))

contador = 0
termo = primeiroTermo

print(f"\nOs {quaTermo} primeiros termos da PA são:")

while quaTermo != 0:
    for _ in range(quaTermo):
        print(termo, end=" ")
        termo += razao
        contador += 1

    print("\n")
    print("Você quer mais termos? [Digite: 0 para sair]")
    quaTermo = int(input("Quantos termos a mais, você deseja: "))

print("\nPrograma Finalizado.")