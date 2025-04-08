import time
time.sleep(1)
frase = str(input("Digite algo: "))
print ("\t-----" * 4)
print ("Você digitou a frase \033[34m{}\033[m".format(frase))
print ("\t-----" * 4)
fraseInvertida = frase[::-1]
if fraseInvertida == frase:
    print("Esse é um Palíndromo!!")
    
else:
    print("Não é um Palíndromo!!")
    
print("\033[1;34m-=-=-=-=-= FIM! =-=-=-=-=-\033[m")