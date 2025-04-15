extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    valor = int(input('Escolha um número de 0 a 20: '))
    if 0 <= valor <= 20:
        print(f'Você digitou o número {extenso[valor]}.')
        break
    else:
        print('Valor inválido. Tente novamente.')

