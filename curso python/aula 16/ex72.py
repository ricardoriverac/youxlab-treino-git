nomeNumeros = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int (input ("Digite um número entre \033[34m0\033[m e \033[34m20\033[m: "))
    if 0 <= numero <= 20:
        break
    print ("Tente novamente.... \033[35mo número precisa ser entre 0 e 20\033[m")
print (f'Você digitou o número: {nomeNumeros[numero]}') 