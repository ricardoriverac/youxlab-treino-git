for c in range(1, 10):
    print(c)
print('FIM')

a=1
while a <10:
    print(a)
    a = a + 1

r = 'S'
nm = 0
while r == 'S':
    nm = int(input('Digite um valor: '))
    conta = nm * 2
    print('O valor desse número multiplicado por 2 é: {}'.format(conta))
    r = str(input('Quer continuar? (S/N): ')).upper()
print ('FIM')
    

n = 1
par = 0
impar = 0
isRodando = True
while isRodando: 
    while n != 0:
     n = int(input('Digite um valor: '))
     if n % 2 ==0:
       par +=1
     else :
         impar +=1
     isRodando = False
print ('Você digitou {} números pares e {} números ímpares.'.format(par, impar))



