from datetime import date
atual =date.today().year
for pess in range(1 , 8):
    ano = int(input('Qual ano você nasceu?  '))
    idade= atual - ano 
    if idade>= 21:
        print('Essa pessoa e de maior')
    else:
        print('Essa pessoa e de menor ')    

