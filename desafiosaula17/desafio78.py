valores = []
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
posicaoMaior = valores.index(maior)
posicaoMenor = valores.index(menor)
print(f'O \033[35mMAIOR NÚMERO\033[m é {maior} e está na \033[36mPOSIÇÃO\033[m {posicaoMaior}')
print(f'O \033[35mMENOR NÚMERO\033[m é {menor} e está na \033[36mPOSIÇÃO\033[m {posicaoMenor}')

    