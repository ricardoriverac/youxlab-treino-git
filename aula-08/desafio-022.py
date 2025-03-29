nome = str(input('escreva seu nome'))

s = nome.upper()
n = nome.lower()
p = nome.replace(" " , "")
d = len(p)

g = nome.split()
#h = nome.find(" ")
k = len(g[0])


print(s)
print(n)
print(d)
#print('seu primeiro nome tem {} letras'.format(h))
print('seu primeiro nome tem {} letras'.format(k))




#frase[9] só o numero aprace a letra no caso: v
#frase[:5] não tem inicio e vai mostrar o caracter 0 vai de 0 até o 5
#frase[9:13] vai mostrar do caracter 9 até o 12, vai excluir o 13 obs
#frase[9:13:2] vai pular de 2 em 2
#frase[15:] vai mostrar do 15 até o ultimo valor
#frase[9::3] vai mostrar do 9 e vai até o final, porem vai pular de 3 em 3
#len = length que é comprimento len(frase)
#frase,find('deo') econtra de onde a palavra começou
#frase.capitalize, vai colocar a primeira letra da palavra em maiusculo
#frase.strip() remove os espaços iniciais e finais
#frase.rstrip() remove os espaços inuteis da direira e não conta o numero de casas