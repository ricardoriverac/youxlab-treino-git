#variaveis :)
contM200 = contM100 = contM50 = contM20 = contM10 = contM5 = contM1 = 0

print('-------------------------\n       BANCO GFI\n-------------------------')
saque = float(input('Qual valor você quer sacar: R$'))
while True:
     if saque >= 200:
         saque -= 200
         contM200 += 1
         
     elif saque >= 100:
         saque -= 100
         contM100 += 1
         
     if saque >= 50:
         saque -= 50
         contM50 += 1
         
     elif saque >= 20:
         saque -= 20
         contM20 += 1
    
     elif saque >= 10:
         saque -= 10 
         contM10 += 1
     
     elif saque >= 5:
         saque -= 5
         contM5 += 1

     elif saque >= 1:
        saque -= 1
        contM1 += 1
        
     if saque == 0:
         break
     
     
print(F'Total de \033[1;31m{contM200}\033[m cédulas de R$200')     
print(F'Total de \033[1;31m{contM100}\033[m cédulas de R$100')
print(F'Total de \033[1;31m{contM50}\033[m cédulas de R$50')
print(F'Total de \033[1;31m{contM20}\033[m cédulas de R$20')
print(f'Total de \033[1;31m{contM10}\033[m cédulas de R$10')
print(F'Total de \033[1;31m{contM5}\033[m cédulas de R$5')
print(f'Total de \033[1;31m{contM1}\033[m cédulas de R$1')
