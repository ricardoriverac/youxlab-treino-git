def contador(*numero):  # * --> Indica um valor indeterminado de parâmetros
    for valor in numero:
        print(f'{valor}', end=' ')
    print('-Fim!')
    tamanho=len(numero)
    print(f'Recebi os valores {numero} e são {tamanho} números ao todo')

contador(7,2,3)  #Resulta a criação de tuplas
contador(1,2)
contador(8,2,9,2)