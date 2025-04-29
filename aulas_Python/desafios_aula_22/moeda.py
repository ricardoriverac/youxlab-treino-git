def moeda(n, formatar=True):
        return f'R${n:.2f}'.replace('.', ',') if formatar else n
    
def metade(n, formatar=True):
    res = n /2
    return moeda(res, True) if formatar else res

def dobro(n, formatar=True):
    res = n * 2
    return moeda(res, True) if formatar else res

def aumentar(preco, porcentagem, formatar=True):
    res = preco + (preco * porcentagem / 100)
    return moeda(res, True) if formatar else res

def diminuir(preco, porcentagem, formatar=True):
   res = preco - (preco * porcentagem / 100)
   return moeda(res, True) if formatar else res

