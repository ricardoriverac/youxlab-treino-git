#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

num = int(input("Qual é o número? "))
numDobro = num*2 #dobro
numTriplo = num*3 #triplo
numRaiz = num ** (1/2) #raiz

print("O dobre de {} vale {}.".format(num, numDobro))
print("O triplo de {} vale {}.".format(num, numTriplo))
print("A raiz de {} vale {:.f}.".format(num, numRaiz)) 