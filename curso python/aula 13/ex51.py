termo = int (input ("Primeiro termo: "))
print ("\t-----" * 4)
razao = int (input ("Razão: "))
print ("\t-----" * 4)
decimo = termo + (10 - 1) * razao
for c in range (termo,decimo,razao):
   print ("\033[34m{}\033[m".format(c), end= " - ")
print ("\033[35mACABOUU!!\033[m")
    