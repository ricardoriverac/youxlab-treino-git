primeiro = float (input('Primeiro Termo: '))
razao = float (input('Razão: '))

termo = primeiro
c = 10
print(f"A PA de {termo} é:", end=" ")
while c > 0:
    print(f"{termo}", end=" ")
    termo += razao
    c -= 1
