num=(int(input('Digite um número:')), 
    int(input('Digite outro:')), 
    int(input('Digite mais um:')),
    int(input('Digite o ultimo: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if  3 in num:
    print(f'O valor 3 apareceu {num.index(3)+1} posições')
else:
    print('O valor 3 não apareceu em nenhum momento')
print('Os valores  pares digitados foram: ', end =' ')
for n in num:
    if n % 2 ==0:
        print(n ,  end=' ' )