from time import sleep
print ('Vamos fazer uma contagem regressiva para soltar fogos!')
sleep(1)
for contagem in range(10, 0, -1):
    print (contagem)
    sleep(1)
print('\033[1;33mFELIZ ANO NOVO!!!!')