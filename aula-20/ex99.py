from time import sleep

def lin():
    print('--'*35)


def maior(valores):
    print()
    print('Analisando os valores que foram passados...')
    print()
    sleep(0.7)
    lin()
    m = max(valores)
    print(f'Foram informados os valores {valores}, e o maior foi o número {m}')
    sleep(1)
    print()


maior(valores = [2,5,6,9])
maior(valores = [0])
maior(valores = [1,5,0,10])
maior(valores = [0,8,9])