for c in range (1,6): #repetir oque está dentro do laço for , o último número o programa ignora 
    # ex 1, 6 tem que fazer (1,7)
    print ("oi") #mensagem detro do laço
print ("FIIM") #mensagem fora do laço

for c in range (0,8,2): #vai contar até 6 de dois em dois
    print (c) #contador
print ("FIM!!")

#n = int (input ("Digite um número: "))
#for c in range (0,n): # entra numero de 0 até a quantidade de (n) que for pedido.
    #print(c)
#print ("FIM!")

i = int (input ("INICIO "))
f = int (input ("FIM "))
p = int (input ("PASSO "))
for c in range (i,f+1,p):
    print(c)
print("FIM")
