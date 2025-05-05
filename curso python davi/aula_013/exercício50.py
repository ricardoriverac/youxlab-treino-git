sm = 0
ct = 0
for c in range(1,7):
    num = int(input('digite o {} valor '.format(c)))
    if num % 2 == 0:
        sm += num
        ct += 1
print('vc informou {} números pares, e o que mais apareceu foi {}' .format(c, num))
