#Faça um programa em python que abre e reproduza o áudio de um arquivo MP3.


import pygame

pygame.mixer.init()

pygame.mixer.music.load("lofiteste.mp3")

pygame.mixer.play()

while pygame.mixer.music_busy():
    continue

pygame.quit()
