#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
num = int(input("Qual é o número? "))

numDobro = num * 2  # Dobro
numTriplo = num * 3  # Triplo
numRaiz = num ** (1/2)  # Raiz quadrada

print("O dobro de {} vale {}.".format(num, numDobro))
print("O triplo de {} vale {}.".format(num, numTriplo))
print("A raiz quadrada de {} vale {:.2f}.".format(num, numRaiz))
