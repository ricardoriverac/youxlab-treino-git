n= float(input('digite um número:'))#converte números para forma decimal 
print(type(n))
print(n)
n= str(input('digite um valor:'))#irá voltar o mesmo valor que foi colocado na var. a diferença e que no str pode colocar palavras com ''. Ex:'olá'
print(type(n))
print(n)
n= bool(input('digite, ou não, um valor:'))#se houver um valor na var. é True se não é False
print(type(n))
print(n)

n= input('digite um número:')#se o valor da var. for números é True se não False 
print(n.isnumeric())
n= input('digite um número:')#se o valor da var. for letras é  True se não False 
print(n.isalpha())
n= input('digite um número:')#se o valor da var. for letras, números ou os dois juntos éTrue se não False 
print(n.isalnum())
n= input('digite um número:')#se o valor da var. for com letras maiúsculas é True se não False 
print(n.isupper())