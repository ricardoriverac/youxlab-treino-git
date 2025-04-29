cont = ('zero', 'um', 'dois', 'tres', 'quatro'
        'cinco', 'seis', 'sete', 'oito' 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze'
        'quinze', 'dezesseis', 'dezessete', 'dezoito'
        'dezenove', 'vinte')    

while True:
    numeros = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numeros <= 20:
        break
    print('Tente Novamente. ', end= '' )
print(f'Você digitou o número {cont[numeros]}')