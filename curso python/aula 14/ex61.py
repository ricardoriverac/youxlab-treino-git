primeiroTermo = int (input ("Primeiro termo: "))
print ("\t-----" * 4)
razao = int (input ("Razão: "))
print ("\t-----" * 4)
contador = 1
numeros = primeiroTermo
mais = 10
while mais !=0:
  while contador <= 10:
      print ("\033[32m{}\033[m".format(numeros), end= " - ")
      numeros = numeros + razao
      contador = contador + 1
print ("\033[35mACABOUU!!\033[m")