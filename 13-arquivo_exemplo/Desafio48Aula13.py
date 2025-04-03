soma = 0
for c in range(1, 501, 2):
    if c%3 ==0:
        print(c , end =  ' ' )
        soma = soma +c
print ('A soma entre os números ímpares e {}'.format(soma))