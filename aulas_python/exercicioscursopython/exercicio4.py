from curses.ascii import isspace


n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaço?', n.isspace())
print('É um número? ', n.isnumeric())
print('E alfabetico? ', n.isalpha())
print('É alfanúmerico? ', n.isalnum())
print('Está em maiúsculo? ', n.isupper())
print('Está em minúsculo? ', n.islower())
print('Está capitalizada? ', n.istitle())

