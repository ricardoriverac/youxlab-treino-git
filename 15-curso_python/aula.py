count = 1
while count <= 10:
    print(count, ' ', end=' ')
    count+=1
print('acabou')

n = 0
cont = 0
while n != 999:
   n = int(input('Digite um número: '))
   cont +=1

s = 0
while True :
   n = int(input('Digite um número: '))
   s += n
   if n == 999:
      break
   
nome = 'jose'
idade = 33
print(f'o {nome} tem {idade} anos')