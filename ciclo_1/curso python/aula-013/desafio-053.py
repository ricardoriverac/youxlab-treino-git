# [::-1] inverte a frase
#re.sub(r'[^a-zA-Z0-9]', '', frase.lower()) remove todos os espaços, acentos da frase
# a expressão "^" significa negação, ou seja: ela não vai incluir o itens que vierem a seguir
#


import re
frase = str(input('Digite uma frase'))
#fraselimpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
#if fraselimpa == fraselimpa[::-1]:
    #print('Essa frase é um palindromo')
#else:
        #print('Essa frase não é um palindromo.')

fraselimpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
while fraselimpa != fraselimpa[::-1]:
    print('Essa frase não é um palindromo, \n tente de novo!')
    frase = str(input('Digite uma frase'))
    fraselimpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
    
else:
    print('{} é um palindromo'.format(frase))




#frase = str(input('Digite sua frase')).strip()
#semesoaço = frase.split()
#if frase == frase[::-1]:
    #print('é um palindromo')
#else:
    #print('não é ')

