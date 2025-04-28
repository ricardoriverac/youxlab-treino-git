numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha = int(input('Digite um número entre 0 e 20: '))

while escolha > 20 or escolha < 0:
    escolha = int(input('Tente novamente! Digite um número entre 0 e 20: '))
    
print(f'Você digitou o número \033[1;31m{numeros[escolha]}\033[m') 