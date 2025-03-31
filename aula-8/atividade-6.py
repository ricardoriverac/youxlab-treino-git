import pygame

# Inicializa o mixer
pygame.mixer.init()

# Carrega um arquivo MP3
pygame.mixer.music.load("musica.mp3")

# Reproduz a música
pygame.mixer.music.play()

# Mantém o programa rodando para o áudio tocar
input("Pressione Enter para parar...")
pygame.mixer.music.stop()
