#Crie um programa que o computador gere as cores do python escolhendo uma aleatoriamente e mostre na tela cor e o nome.

#Randozima um número inteiro
from random import randint 

computador = randint(0,7)
#Randozima entre 0 a 7 

#Lista das cores
listadeCores = ['\033[1;30mBranco\033[m \033[40m.\033[m' , '\033[1;31mVermelho\033[m \033[41m.\033[m' , '\033[1;32mVerde\033[m \033[42m.\033[m' , '\033[1;33mAmarelo\033[m \033[43m.\033[m ' , '\033[1;34mAzul\033[m \033[44m.\033[m ' , '\033[1;35mRoxo\033[m \033[45m.\033[m ' , '\033[1;36mCiano\033[m \033[1;46m.\033[m ' , '\033[1;37mCinza\033[m \033[1;47m.\033[m ']

#Colocando cores no python.

#Exemplo "\033[0;30;40m"

# \033[m = Comando para colocar cores. 

# "0 = O estilo da letra" 

# "30 = A cor dos textos "

# "40 = A cor das letras "

# "m" Entre os [] você deve sempre colocar a letra "m"
   
#Troca os números pela as cores
print(listadeCores[computador])
