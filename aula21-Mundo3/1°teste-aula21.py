def fatorial(numero=1):  #Caso não informe numero ele vai valer 1 pois VIROU UM VALOR OPICIONAL 
    fator=1  #variável local
    for contador in range (numero,0,-1):
        fator*=contador
    return fator
numero=int(input('Digite um número: '))
print(f'O fatorial de {numero} é {fatorial(numero)}')

