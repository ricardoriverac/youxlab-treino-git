num=int(input('M ediga um número e direi se ele e par ou impar: '))
print('--'*20)
resultado = num % 2
if resultado == 0: 
    print('Seu numero {} e par meu nobre '.format(num))
else:
    print('Você possui um numero impar ')