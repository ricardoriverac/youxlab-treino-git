from datetime import datetime
maior= 0
menor= 0

for anos in range(0,3):
    print("\n")
    dia=int(input(f"Digite o dia do nascimento, da {anos+1} pessoa: "))
    mes=int(input(f"Digite o mes do nascimento, da {anos+1} pessoa: "))
    ano=int(input(f"Digite ano do nascimento, da {anos+1} pessoa: "))

    datanasc= datetime(ano,mes,dia)
    hoje= datetime.now()
    idade = hoje.year - datanasc.year
    if (hoje.month,hoje.day) < (datanasc.month, datanasc.day):
        idade -= 1
    if idade >= 18:
        maior += 1    
    else:
        menor += 1
print(f"\nPessoas maiores de idade: {maior}")
print(f"Pessoas menores de idade: {menor}\n")


