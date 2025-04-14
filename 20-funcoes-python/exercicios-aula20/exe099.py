def maior(*num):
    maior = 0
    for numero in num:
        if numero == 0:
            maior = numero 
        else:
            if numero > maior:
                maior = numero
    print(f'Os valores {num}')
    print(f'O maior valor é {maior}')

maior(1,2,5,6,7)
maior(3,1,2)
maior(9,1,2,4,5,10)