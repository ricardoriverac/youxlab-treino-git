n1 = input ('Digite algo')
print(n1, 'É do tipo primitivo', type(n1))
print(n1, 'Possui apenas números?', n1.isnumeric(), '!')
print(n1, 'Possui apenas letras?',  n1.isalpha(), '!')
print(n1, 'Possui letra ou número?', n1.isalnum())
print(n1, 'Possuia apenas letras maiúsculas?', n1.isupper())
print(n1, 'Possui apenas letras minúsculas?', n1.islower())

