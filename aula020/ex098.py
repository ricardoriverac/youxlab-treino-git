from time import sleep

def contagem(inicio,fim,passo):
    print(f'\n Contagem de {inicio} até {fim} de {passo} em {passo} ')

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:  
        contador = inicio

        while contador <= fim:
            print(f'{contador}',end = ' ',flush=True)

            contador += passo
            sleep(0.5)

    else:
        contador = inicio
        while contador >= fim:
            print(f'{contador} ',end =' ',flush = True)

            contador -= passo
            sleep(0.5)

contagem(1,10,1) 
contagem(10,0,2)
print('Sua vez de escolher: ')

usuarioInicio = int(input('Inicio: '))
usuarioFim = int(input('Fim: '))
usuarioPasso = int(input('Em quanto em quanto: '))

contagem(usuarioInicio,usuarioFim,usuarioPasso)