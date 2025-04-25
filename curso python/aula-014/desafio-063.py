num = int(input('Quantos termos quer mostrar?'))
primeiroNum = 0
segundoNum = 1
cont = 1 #define um contador
while cont <= num:
    print(f'{primeiroNum}', end=' ') #vair printar o a seguencia na horizontal
    calculo = primeiroNum + segundoNum #variavel que vai somar os anteriores 
    primeiroNum = segundoNum
    segundoNum = calculo
    cont += 1

