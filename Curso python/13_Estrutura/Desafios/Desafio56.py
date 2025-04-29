mulherMenos20 = 0
somaidade=0
media= 0
maiordidadehomem= 0
nomevelho= ""
for p in range(1,5):
    print(f"------ {p} PESSOA ------")
    nome = str(input("Nome: ")).strip()
    idade= int(input("Idade: "))
    sexo= str(input("Sexo[M/F]: ")).strip().upper()
   
    somaidade += idade 
    
    if sexo == "M" and idade > maiordidadehomem:
        maiordidadehomem = idade
        nomevelho = nome
        
    if sexo == "F" and idade < 20:
        mulherMenos20 += 1
        
media = idade / 4     
print(f"A media de idade do grupo e {media}")

if nomevelho:
    print(f"O homem mais velho e {nomevelho} com {maiordidadehomem} anos.")
else:
    print("Nao a homem velho")

print(f"Ha {mulherMenos20} mulheres com menos 20 anos.")