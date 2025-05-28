a = int(input(' diga 3 números, o primeiro: '))
b = int(input('segundo: '))
c = int(input('terceiro : '))
mnr = a
if b < a and b < c :
    mnr = b
if c < a and c < b :
    mnr = c
mir = a
if b > a and b > c :
    mir = b
if c > a and c > b :
    mir = c
print(f'O maior é {mir}')
print(f'O menor é {mnr}')     
      