def forma(msg):
    a = f'R${msg:.2f}'.replace('.',',')
    return a

def metade(n, show=False):
    m = n / 2
    if show:
        return forma(m)
    return m

def dobro(n, show=False):
    d = n * 2
    if show:
        return forma(d)
    return d

def aumentar(n, p, show=False):
    a = n + (n * (p / 100))
    if show:
        return forma(a)
    return a

def reduzir(n, p, show=False):
    a = n - (n * (p / 100))
    if show:
        return forma(a)
    return a
import Desafio109
v = float(input('Digite o preço: R$'))
print(f'A metade de {Desafio109.forma(v)} é {Desafio109.metade(v, True)}')
print(f'O dobro de {Desafio109.forma(v)} é {Desafio109.dobro(v, True)}')
print(f'Aumentando 10%, temos {Desafio109.aumentar(v, 10, True)}')
print(f'Diminuindo 13%, temos {Desafio109.reduzir(v, 13, True)}')