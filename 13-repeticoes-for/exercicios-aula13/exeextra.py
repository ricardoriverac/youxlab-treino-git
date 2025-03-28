import pygame
import emojis
from time import sleep
texto = "Vamos fazer a contagem regressiva para o ano de 2025???? :smiley:!"
texto2 = "FELIZ ANO NOVO!!! :fireworks: :sparkler:"
resultado = emojis.encode(texto)
resultadodoTexto2 = emojis.encode(texto2)
#print(emojis(f'Vamos fazer a contagem regressiva para o ano de 2025??????'))
print(resultado)
for c in range(10,-1,-1):
    sleep(1)
    print(f'\033[35m{c}\033[m')
print(f'\033[31m{resultadodoTexto2}\033[m')  
pygame.mixer.init()
pygame.mixer.music.load("explosion-312361.mp3")
pygame.mixer.music.play()

input('\033[36mpressione enter para sair\033[m')

