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

def format(n, formatar= ''):
    if formatar == 's':
        n = (f'R${n:.2f}')
    elif formatar != 'n':
        print('Inválido!')
    return n

def formata(n):
    n = (f'R${n:.2f}')
    return n

def resumo(n):
   
    print(f'{"Preço analisado:":<20}{formata(n):>20}')
    print(f'{"Dobro do preço:":<20}{formata(dobro(n)):>20}')
    print(f'{"Metade do preço:":<20}{formata(metade(n)):>20}')
    print(f'{"10%"" de aumento:":<20}{formata(aumentar(n)):>20}')
    print(f'{"15%"" de redução:":<20}{formata(diminuir(n)):>20}')
    print('--'*20)
    

def titulo(txt):
    print('--'*20)
    print(txt.center(40))
    print('--'*20)
