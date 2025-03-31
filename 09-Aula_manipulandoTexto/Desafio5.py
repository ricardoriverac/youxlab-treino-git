frase =str(input('Me diga seu nome ')).upper()
print(' a letra a aparece {}'.format(frase.count('A')))
print('a  letra A apareceu na pocicoes {}'.format(frase.find('A')+1))
print('a ultima letra A que aparece e {}'.format(frase.rfind('A')+1))