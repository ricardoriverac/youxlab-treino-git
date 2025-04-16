valores=[]
while True:
    resposta=str(input('Você deseja continuar? [S/N]: ').upper())

    if resposta == 'N':
        break

    valor=int(input('Digite um valor: '))

    if valor in valores:
        print('O valor esta dentro ')

    else:
        valores.append(valor)
print(valores)


    # for numero in  valores:
    #     if numero  in valores:
    #         print('O numero digitado já está dentro...')







        


