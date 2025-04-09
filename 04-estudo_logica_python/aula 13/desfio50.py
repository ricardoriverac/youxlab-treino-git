for i in range (1,7):
    soma=0
    numero=int(input('Digite um numero inteiro :'. format(i)))
    if numero % 2 ==0 :
        soma += numero

print('A soma dos números pares digitados é {}'.format(soma))