numero =  0
soma = 0
contadorNumeros = 0
while True: 
    numero = int (input("Digite um numero, \033[36m[999\033[m para sair do programa] "))
    if numero == 999: 
        break 
    soma += numero
    contadorNumeros += 1
print (f" Você digitou \033[36m{contadorNumeros}\033[m números, a soma deles vale: \033[33m{soma}\033[m") 