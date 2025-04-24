ano = int(input("Coloque um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} e um ano bissexto.")
else:
    print(f"{ano} não e um ano bissexto.")