import pygame 
from time import sleep
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()
while pygame.mixer.music.get_busy():
    sleep (1)
