def escreva(texto):
    tamanho = len(texto)
    print("~" * (tamanho + 4))
    print(f"  {texto}")
    print("~" * (tamanho + 4))
texto_usuario = input("Digite um texto: ")
escreva(texto_usuario)