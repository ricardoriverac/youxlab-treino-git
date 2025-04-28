from random import randint
sorteados = []

def sorteio(sorteados):
    
        while len(sorteados) != 5:

            numero = randint(1,99)
            sorteados.append(numero)

        print(sorteados)

def somaPares(sorteados):
    soma = 0
    valor = 0
    for valor in sorteados:
         if valor % 2 == 0:
            soma += valor 

    print(soma)
            
        
print(sorteados)




    

sorteio(sorteados)
somaPares(sorteados)