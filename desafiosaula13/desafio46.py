from time import sleep
print('{}CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO:{}'.format('\033[35m', '\033[m'))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{}FOGOS DE ARTIFÍFICIO!!!{}'.format('\033[36m', '\033[m'))
