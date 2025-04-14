def escreva(msg):
    c = 0
    linhas = ""
    while c < len(msg):
        linhas += "~"
        c += 1
    return print(linhas), print(msg), print(linhas)


escreva("Gustavo guanabara")
escreva("Curso de pyton no youtube")
escreva("cev")