numero1=int(input('digite um numero:'))
numero2=int(input('digite outro numero:'))
numero3=int(input('digite outro numero:'))
maior= numero1
menor=numero1
if maior <numero1:
   maior = numero2
if maior < numero3: 
	maior = numero3
if menor > numero2:
	menor = numero2
if menor > numero3:
	menor = numero3
print ('O maior número é:  %d ' % maior)
print ('O menor número é:  %d ' % menor)