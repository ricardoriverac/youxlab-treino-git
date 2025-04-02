text = str(input('Digite uma frase: ')).upper()
quantidade = (text.count('A'))
posicao1 = (text.find('A')+1)
posicao2 = (text.rfind('A')+1)
print(f'''a letra A aparece {quantidade} vezes na frase
Aparece pela primeira vez na posição {posicao1} 
e aparece pela última vez na posição {posicao2}''')