termo = int(input("Digite o primeiro termo: \n"))
razao = int(input("Digite a razão da PA, por favor: \n"))
contador = 1
termo = 0
user = -1
tam = 10 

while True:
    while contador < tam:
        termo += razao
        contador+= 1
        print(termo)
    user = int(input("Digite mais termos:"))

    if user == 0:
        break
    user += contador
    tam = user

print("Fim.")