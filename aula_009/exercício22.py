nome = str(input("qual o seu nome? "))
letrasNoNome = len(nome)
#primeiroNome = 
mkj = nome.lower()
lpc = nome.upper()

print("seu nome em maiúsculo: {}.".format(lpc)) 

print("seu nome em minúsculo: {}.".format(mkj))

print("seu nome tem {} espacos.".format(nome.find(" ")))

print("o nome tem ao todo {} letras.".format(letrasNoNome))

semEspaco = len(nome.replace(" ", ""))
print("Seu nome contem {} letras sem os espaços.".format(semEspaco))