#OPERADORES ARITMÉTRICOS
#Ordem de precedência
#1 : ( )
#2 : **
#3 : * , / , // , %
#4 : + , -
nome = input ("Qual é o seu nome: ")
print ("prazer em te conhecer {}".format(nome))
#nome = input ("Qual é o seu nome: ") 
#print ("prazer em te conhecer {:20}".format(nome))20 caracteres
n1 = int (input("Digite um número: "))  #entrada do primeiro número
n2 = int (input("Digite outro número: "))  #entrada do segundo número
s = n1 + n2 # SOMA
m = n1 * n2 # MULTIPLICAÇÃO
d = n1 / n2 # DIVISÃO
di = n1 // n2 # DIVISÃO INTEIRA
e = n1 ** n2 # EXPONENCIAÇÃO
print ("A soma é {}, o produto é {} e a divisão é {} ". format(s,m,d))
print ("divisão inteira {} e potência {}".format(di,e))