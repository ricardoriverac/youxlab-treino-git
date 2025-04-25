from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo
    print('\n' + '\033[35m-\033[m'*40)
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}:  << fim') 
    if inicio < fim:
        numeroAtual = inicio
        while numeroAtual <= fim:
            print(numeroAtual, end=' ')
            sleep(0.3)
            numeroAtual += passo
    else:
        numeroAtual = inicio
        while numeroAtual >= fim:
            print(numeroAtual, end=' ')
            sleep(0.3)
            numeroAtual -= passo
    print('\n' + '\033[35m-\033[m'*40)
contador(1, 10, 1)
contador(10, 0, 2)
print('\n' + '\033[35m-\033[m'*40)
print ('-=' * 4, f'\033[35m sua vez de personalizar a contagem \033[m','-=' * 4 )
valorInicio = int(input('Início: '))
valorFim = int(input('Fim: '))
valorPasso = int(input('Passo: '))
contador(valorInicio, valorFim, valorPasso)
print('\n' + '\033[35m-\033[m'*40)
