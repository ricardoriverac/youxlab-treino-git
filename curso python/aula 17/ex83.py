expressao = str (input("Digite sua expressão: "))
contadorAberto = 0
contadorFechado = 0
for i in expressao:
   if  i == "(":
    contadorAberto += 1
   elif   i == ")":
    contadorFechado += 1
if  contadorAberto ==  contadorFechado:
    print ("Sua expressão está correta!!!")
else:
    print ("Sua expressão está incorreta!!!")
