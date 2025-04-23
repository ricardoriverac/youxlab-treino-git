def aumentar(n):
    n += (n/100) * 10 
    return n

def diminuir(n):
    n -= (n/100) * 15
    return n 

def dobro(n):
    n *= 2
    return n

def metade(n):
    n /= 2
    return n

def format(n):
    n = (f'R${n:.2f}')
    return n