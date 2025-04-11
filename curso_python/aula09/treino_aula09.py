# Mostra a palavra escrita
frase = 'Curso em Vídeo Python'
print (frase)

# Mostra a quarta letra
frase = 'Curso em Vídeo Python'
print (frase[3])

# Mostra da letra 4 até a letra 12
frase = 'Curso em Vídeo Python'
print (frase[3:13])

# Mostra do início até a letra 12
frase = 'Curso em Vídeo Python'
print (frase[:13])

# Mostra da letra 12 até o final
frase = 'Curso em Vídeo Python'
print (frase[13:])

# Mostra da letra 0 até a 15 de 2 em 2
frase = 'Curso em Vídeo Python'
print (frase[1:15:2])

# Mostra a string inteira de 2 em 2
frase = 'Curso em Vídeo Python'
print (frase[::2])

# Para mostrar um texto grande
print ("""25 And the Lord spake unto the Angel that guarded the eastern gate, 
saying 'Where is the flaming sword that was given unto thee?'
26 And the Angel said, 'I had it here only a moment ago, I must have put it down 
some where, forget my own head next.'
27 And the Lord did not ask him again.""")

# Para mostrar quantas vezes uma letra aparece
frase = 'Curso em Vídeo Python'
print (frase.count('o'))

# Torna maiúscula alguma letra e conta quantas vezes ela aparece (combinação)
frase = 'Curso em Vídeo Python'
print (frase.upper().count('O'))

# Mostra o tamanho da frase
frase = 'Curso em Vídeo Python'
print (len(frase))

# Troca as palavras selecionadas
frase = 'Curso em Vídeo Python'
print (frase.replace('Python', 'Android' ))

# Verifica se a palavra está na string
frase = 'Curso em Vídeo Python'
print ('Curso' in frase)

# Mostra em qual posição está
frase = 'Curso em Vídeo Python'
print (frase.find('Vídeo' ))

# Cria uma lista com todas as palavras
frase = 'Curso em Vídeo Python'
print (frase.split())

# Mostra uma letra de uma palavra
frase = 'Curso em Vídeo Python'
dividido =frase.split()
print(dividido[2][3])