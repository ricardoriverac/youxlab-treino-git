par = 0
imp = 0

for c in range(1,7):
    num =  int(input('Digite seu {}º número: '.format(c)))
    
    if num % 2 == 0:
        par += num

    else:
        imp += 1
        
        
print('Se eu somar apenas os números pares vai dar: {}\nQuantidade de números impares: {}'.format(par,imp))
    