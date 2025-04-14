print("====="*3)
print(" GERADOR DE PA ")
print("====="*3)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = primeiro
conta = 1
while conta <= 10:
    print(f"{termo}")
    termo += razao
    conta += 1
print("====="*3)
print("      FIM")
print("====="*3) 