num = list()
pares = list()
impares = list()
while True:
    num.append(int(input("Digite um numero: ")))
    escolha = str(input("Quer continuar? [S/N]: "))
    if escolha in "Nn":
        break
for i,  v in  enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
    print("-="*20)
    print(f" A lista  completa e  {num}")
    print(f" A lista de pares e {pares}: ")
    print(f" A lista de impares e {impares}")
      
        