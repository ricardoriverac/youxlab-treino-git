def maior(*numeros):
    def linhas():
        print('<>'*20)

    maiorNumero = 0


    for numero in numeros:
        if numero > maiorNumero:
            maiorNumero = numero
    linhas()
    print(f'Dentre {numeros} esse e o número maior: {maiorNumero}')  
    linhas()



maior(4,6,3,6,4,9,2,1)
maior(2,4,66,33,55,44,3)
maior(3,5,2)