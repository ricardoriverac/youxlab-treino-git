primeiroTermo = int (input ("Primeiro termo: "))
print ("\t-----" * 4)
razao = int (input ("Razão: "))
print ("\t-----" * 4)
contador = 1
numeros = primeiroTermo
mais = 10
total = 0
while mais !=0:
   total = total + mais
   while contador <= total: 
      print ("\033[32m{}\033[m".format(numeros), end= " - ")
      numeros = numeros + razao
      contador = contador + 1
   print ("...")
   print ("Para encerrar digite 0...")
   mais = int (input("Você quer mostrar mais algum termo ? "))
print (("Progressão finalizada com \033[36m{}\033[m termos mostrados.".format(total)))
print ("\033[35mACABOUU!!\033[m")