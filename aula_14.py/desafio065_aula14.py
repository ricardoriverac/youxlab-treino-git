flag = False
somador = 0
contador = 0
while flag == False:
    numero = int(input('Digite um número... [Digite 999 para quebrar a soma]: \n'))
    if numero ==999:
        flag = True
    else:
        somador += numero
        contador += 1
        print('soma: {}.'.format(somador))
    print('numeros digitados: {}.'.format(contador))