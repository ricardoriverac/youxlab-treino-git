from time import sleep
def lin():
     
     print('=' * 30)
def contador():
    lin()
    i=int(input('Inicio: '))
    lin()
    f=int(int(input('Fim: ')))
    lin()
    p=int(input('Passo: '))
    for c in range(i , f+1 , -p):
         print(c , end =' ')
    lin()

print('Contagem de 1 ate 10 , em 1 em 1')
lin()
for c in range (0 , 11):
    print(c , end =' ')
print()
lin()
print('Contagem de 10 ate 1, em 2 em 2')
for r in range (10 , 0 , -2):
      print(r , end=' ')
print()

contador()
lin()

