#operadores aritméticos
#a= 5+3*2
#print(a)

#b= 5**2
#print(b)

#c= 19/2
#print(c)

#d= 18%7
#print(d)

#e= 122%3
#print(e)

#f= 4**3
#print(f)

#g= pow(4,3)
#print(g)

#h= 81**(1/2)
#print(h)

#i= 25**(1/2)
#print(i)

#j= 127**(1/3)
#print(j)

#k= 'Oi' + 'Olá'
#print(k)

#l= 'Hi!' *5
#print(l)

nome = str(input('Qual é o seu nome?'))
print('Prazer em te conhecer{:^20}!'.format(nome))

n1= int(input('Um valor:'))
n2= int(input('Outro valor:'))
s= n1+n2
m= n1*n2
d= n1/n2
di= n1//n2
e= n1**n2
print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira {} \n e potência {}'.format(di,e))

 







