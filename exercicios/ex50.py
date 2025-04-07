soma = 0
cont = 0
for c in range (0,6):
   num = int (input ("Digite um número: "))
   if num % 2 == 0:
        cont += num
print ("A soma dos números pares é: \033[31m{}\033[m".format(cont))
 
       
