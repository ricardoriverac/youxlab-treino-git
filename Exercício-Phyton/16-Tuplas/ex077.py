palavras = ['banana', 'fini', 'guaraná']

for palavra in palavras:
    print(f"Palavra: {palavra}")
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f"Vogal: {letra}")
