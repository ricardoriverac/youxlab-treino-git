#aprendendo comandos
frase='Sophia Del Santo de Carvalho'
print(frase)#frase toda

print(frase[3])#letra que ocupa o espaço 3

print(frase[6:29])#começa do espaço 6 e vai até o 29

print(frase[1:29:2])#começa do espaço 1, vai até o 29 saltando espaços de um em um

print(frase[::2])#frase toda saltando de um em um

print(frase.upper().count('O'))#quantas vezes aparece a letra "o"

print(len(frase))#quantidade de letras (contando com os espaços) 

print(len(frase.strip()))#retira espaços indesejados das fases

print(frase.replace('Sophia','Sosô'))#subistitui a palavra "Sophia" por "Sosô"
# este comando NÃO altera a frase  inicial, para alaterar é preciso salvra a alteração assim:
# frase = print(frase.replace('Sophia','Sosô')) 

print('Sophia' in frase)#confere se tem tal palavra na frase, se sim volta True se não é False

print(frase.find('Santo'))#Da a posição de palavra "Santo"  na frase neste caso

print(frase.lower().find('Santo'))#.lower() --> letras minúsculas (neste caso NÃO existi a palavra "Santo" com letras minúsculas então aparecerá -1)

#Para inserir um texto de uma vez só basta usar 3 aspas
print('''Python é uma linguagem de programação de alto 
nível, orientada a objetos, que pode ser usada 
em diversas áreas, como desenvolvimento web, 
ciência de dados e automação. ''')


