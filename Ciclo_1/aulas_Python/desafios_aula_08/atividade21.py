import pygame

pygame.init()

pygame.mixer.music.load('flor.mp3')
pygame.mixer.music.play()
pygame.event.wait()