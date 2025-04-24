extensos = ('zero ' , 'um' , 'dois' , 'três' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'quartoze' , 'quinze' , 'dezesseis' , 'dezessete' , 'dezoito' , 'dezenove' , 'vinte' )
num = int(input('Digite um número entre 0 a 20: '))
while num > 20 or num < 0 : 
    num = int(input('Tente novamente. Digite um número Entre 0 e 20: '))
for cont in range(0 , len(extensos)):
    if num == cont :
        print(f'Digitou o número  {extensos[num]}')