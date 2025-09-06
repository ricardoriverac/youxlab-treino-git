from random import randint
pc = randint = (0, 10)
print('advinhe o número de 0 a 10. ')
acertou = False
palp = 0
while not acertou:
    jg = int(input('chute um número: '))
    palp += 1
    if jg == pc:
        acertou:True
print('acertou com {} tentativas.' .format(palp))
