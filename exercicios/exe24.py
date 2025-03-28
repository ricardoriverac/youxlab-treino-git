#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "LAVRAS".

#FORMA QUE O GUANABARA FEZ
#cid = str(input("Em que cidade você nasceu? ")).strip()
#print(cid[:6].upper() == "LAVRAS")

cid = str(input("Qual cidade você nasceu? ")).lower()

localNascido = "lavras"

if cid in [ "lavras" ]:
    print("Você nasceu em {}, no estado de MG.".format(localNascido))
else:
    print("Você não nasceu neste local!")
