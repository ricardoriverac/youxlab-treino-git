def leiaNumero(mensagem):
    while True:
        numero=input(mensagem)


        if numero.isdigit():
           return int(numero)
        
        else:
            print('\033[;31m Erro digite um número valido.\33[m ' )


numero =leiaNumero('Digite um valor: ')
print(f'Você digitou o número {numero}')

