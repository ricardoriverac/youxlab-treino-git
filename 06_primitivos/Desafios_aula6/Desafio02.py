a= input("Digite algo ")
print("O tipo primitivo desse valor e", type(a))
print("So tem espaços? ", a.isspace()) 
print("E um numero ?" , a.isnumeric())
print("E alfabetico ?" , a.isalpha())
print("E alfanumeric?" , a.isalnum())
print("Esta em maiusculas? ", a.isupper())
print("Esta em minusculas?", a.islower())
print("Esta capitalizada? ", a.istitle())