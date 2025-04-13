from random import randint

print("Ola!...")
print("Sou seu computador, eu pensei em um numero de 1 a 10...")
numerodopc = randint(0,10)
print("Tente adivinhar....")
acertou = False
while not acertou:
    numero = int(input("Qual e seu palpite? "))
    if numero == numerodopc:
        print("Parabens voce acertou! ")
        break

            

