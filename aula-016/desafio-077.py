lista = []
vogais = 'aeiou'

# Coleta das palavras
while True:
    nome = input('Digite palavras: (digite "pare" para parar): ')
    if nome.lower() == 'pare':
        break
    lista.append(nome)

# Mostra as palavras digitadas
print("\nPalavras digitadas:")
for palavra in lista:
    print(f"- {palavra}")

# Mostra as vogais de cada palavra
print("\nVogais em cada palavra:")
for palavra in lista:
    vogais_da_palavra = [letra for letra in palavra.lower() if letra in vogais]
    print(f"{palavra}: {' '.join(vogais_da_palavra) if vogais_da_palavra else 'Nenhuma vogal'}")



# lista = []
# vogal = []
# while True:
#     nome = str(input('Digite palavras: "pare" para parar.'))
#     lista.append(nome)
#     if nome == 'pare':
#         break
# for nome in lista:
#     if nome.lower() in 'a' 'e' 'i' 'o' 'u':
#         vogal.append(lista)
#     print(vogal)
        # print(f'A Palavra {nome} tem {vogal}')
