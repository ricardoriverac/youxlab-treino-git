termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão'))
n = 11
an = termo + (n - 1) * razao
for c in range(termo, an, razao):
    print(c)

    