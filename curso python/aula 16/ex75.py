valores = int (input ("Digite o PRIMEIRO número: ")), int (input ("Digite o SEGUNDO número: ")), int (input ("Digite o TERCEIRO número: ")), int (input ("Digite o QUARTO número: "))
print(f"Os valores digitados foram: {valores}")
print (f"O valor 9 apareceu {valores.count(9)} vezes")
if 3 in valores:
    print (f"O número 3 apareceu a primeira vez na {valores.index(3)+1}º posição")
else:
    ("O valor 3 não foi digitado em nenhuma posição.....")
print (f"Números pares digitados: ", end=' ')
for numeroPar in valores:
    if numeroPar % 2 == 0:
     print (numeroPar, end= ' ')