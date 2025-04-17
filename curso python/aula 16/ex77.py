palavras = ('casa', 'carro', 'gato', 'cozinha', 'janela')
vogaisPalavras = {}
for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra in 'a,e,i,o,u':
            vogais.append(letra)
    vogaisPalavras[palavra] = vogais
print(f"{'Palavra':<10} {'Vogais'}") 
print("-" * 20)  
for palavra, vogais in vogaisPalavras.items():
    print(f"{palavra:<10} {', '.join(vogais)}")
