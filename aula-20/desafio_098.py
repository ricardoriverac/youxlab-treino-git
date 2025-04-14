from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')
        sleep(0.5)
    print()




contador(1,10,0)
contador(10,0,2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))