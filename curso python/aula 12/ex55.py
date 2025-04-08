list = [ ]
for kg in range (1,6):
    peso = int (input ("Qual é o seu peso ? ").format(kg))
    list.append(peso)
maior = max(list)
menor = min(list)
print ("Maior peso {}".format(maior))
print ("Menor peso {}".format(menor))