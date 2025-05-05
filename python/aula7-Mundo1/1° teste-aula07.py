n1= int(input('digite o primeiro n°:'))
n2= int(input('digite o segundo n°:'))
s= n1 + n2
sb= n1 - n2
m= n1 * n2
d= n1 / n2
p= n1 ** n2
di= n2 // n2
r= n1 % n2
print ('a soma é {},\n subtração é {},\n multiplicação é {}, divisão é {}'.format(s,sb,m,d), end='' ) 
print (' potência é {}, divisão inteira é {}, resto é {}'.format(p,di,r))
# end='' --> comando para não pular linha e fazer um texto continuo
#\n --> '' para colocar informações uma de baixo das outras