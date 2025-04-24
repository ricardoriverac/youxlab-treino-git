
def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def metade(valor):
    return valor / 2

def dobro(valor):
    return valor * 2

def aumentar(valor, percentual):
    return valor + (valor * percentual / 100)


p = float(input('Digite o preço em R$ '))

print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')
