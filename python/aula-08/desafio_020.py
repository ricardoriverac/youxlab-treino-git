from random import shuffle
n1= str(input("primeiro aluno: "))
n2= str(input("segundo aluno: "))
n3= str(input("terceiro aluno: "))
n4= str(input("quarto aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A orddem de apresentação será ")
print(lista)