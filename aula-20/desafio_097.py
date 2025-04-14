def Escreva(palavra):
    tamanho = len(palavra)+4
    print("-"*(tamanho))
    print(f'  {palavra.center(tamanho)}')
    print("-"*(tamanho))

palavra = input("Digite qualquer palavra: ")
print(Escreva(palavra=palavra))