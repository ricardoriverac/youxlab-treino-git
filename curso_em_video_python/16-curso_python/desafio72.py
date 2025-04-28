numeroExtenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
numero = 0
while True:
    numero = int(input('Escolha um número de 0 a 20: '))
    if numero >=0 and numero <=20:
        break
    print('Algo deu errado, tente novamente. ')
print (f'Você digitou o número {numeroExtenso[numero]}.')