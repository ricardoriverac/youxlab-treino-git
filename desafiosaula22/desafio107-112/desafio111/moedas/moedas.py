def aumentar(preço=0, taxa=0, formato = False):
    resultado = preço + (preço * taxa/100)
    return resultado if formato is False else moeda(resultado)

    
def diminuir(preço=0, taxa=0, formato = False):
    resultado = preço - (preço * taxa/100)
    return resultado if formato is False else moeda(resultado)
    
def dobro (preço=0, formato = False):
   resultado = preço * 2
   return resultado if formato is False else moeda (resultado)
    
def metade(preço=0, formato = False):
    resultado = preço/2
    return resultado if formato is False else moeda(resultado)    

def moeda(preço=0, moeda='R$'):
    True
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço, aumento, redução):
    print('-'*40)
    print('\033[1;35mRESUMO DO VALOR\033[m'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('-'*40)
