numeroExtenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
numero = int(input('Escolha um número de 0 a 20: '))
reserva = 21
while numero >=0 and numero <=20:
    print (f'O número {numero} por extenso é: ')
    if numero == 1:
        print (numeroExtenso[1])
    if numero == 0:
        print(numeroExtenso[0])
    if numero ==3:
        print(numeroExtenso[3])
        
     
   