nome = str (input ("QUal seu nome ? "))
if nome == gustavo: #estrutura SE
    print ("Que nome lido você tem, !") #vai ler essa esse comando
else: #Estrutura SENÃO
    print ("Bom dia, {}".format(nome))
    print ("Seu nome é tão normal!")

n1 = float (("Digite o primeiro número: "))
n2 = float (("Digite outro número: "))
m = (n1 + n2)/2
print ("A sua média foi {:.1f}".format(m))
if media >= 6:
    print ("Sua média foi boa, PARABÉNS!")
else:
    print ("Sua média foi ruim, ESTUDE MAISS!")