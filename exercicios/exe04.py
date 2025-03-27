#Dissecando uma Variável

a = input("digite algo: ")

print("o tipo primitivo e: ", type(a))

print("So tem espaços? ", a.isspace())
print("E um número? ", a.isnumeric())
print("E alfabetico? ", a.isalpha())
print("É alfanumerico?", a.isalnum())
print("Esta em maiuscula?", a.isupper())
print("Esta minuscula?", a.islower())
print("Esta centralizada?", a.istitle())

