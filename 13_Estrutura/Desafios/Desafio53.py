frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junta= "".join(palavras)
trocar = ""
for letra in range(len(junta)- 1, -1, -1):
    trocar += junta[letra]
if trocar == junta:
    print("PALINDROMO")
else:
    print("Nao e um PALINDROMO")
