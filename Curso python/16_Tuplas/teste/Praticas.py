#usado para mostrar posição 
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim" ) 
for cont in range (0, len (lanche)):
   print(f"Eu vou comer {lanche[cont]} na posição {cont}")
 #sem numeraçao 
for comida in lanche:
    print(f"eu vou comer{comida}")
print("Comi muito!")
# variavel mas com a opçao de numerar
for pos ,comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("Comi muito")
