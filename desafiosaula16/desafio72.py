extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Escreva um número entre \033[33m0 e 20:\033[m '))
    if numero>=0 and numero<=20:
        print(f'O número {numero} em extenso é \033[35m{extenso[numero]}\033[m')
        break
    else:
        print('Digite um número entre \033[33m0 a 20!\033[m Tente novamente ')
        
        