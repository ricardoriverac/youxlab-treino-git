from time import sleep
num = int(input('Digite um número: '))

def contador(num):
    print(num)
    sleep(0.3)
    while True:
        if num != 0:
            num -= 1
            print(num)
            sleep(0.3)
        else:
            break
contador(num)