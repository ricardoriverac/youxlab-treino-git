print("====="*3)
print(" GERADOR DE PA ")
print("====="*3)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = primeiro
conta = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while conta <= total:
        print(f"{termo}")
        termo += razao
        conta += 1
    print("====="*3)
    print("      FIM")
    print("====="*3)
    mais = int(input("Quantos termos voce quer mostrar?: "))