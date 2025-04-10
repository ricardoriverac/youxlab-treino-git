continuacao = 'S'
numero = 0
contadorNumeros = 0
soma = 0
list = [ ]
while continuacao == "S":
    numero = int (input ("Digite um número: "))
    continuacao = str (input ("Quer continuar [S/N] ? ")).strip().upper()
    contadorNumeros += 1
    soma += numero
    media = soma / contadorNumeros  
    list.append(numero)
    maior = max(list)
    menor = min(list)
print ("FIIM")
print ("foram digitados \033[31m{}\033[m números, e a média entre eles é de \033[31m{:.2f}\033[m. ".format(contadorNumeros,media))
print ("O maior número digitado foi \033[36m{}\033[m , e o menor número digitado foi \033[36m{}\033[m.".format(maior,menor))