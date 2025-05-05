def formatar(txt):

    text = str(txt)

    pos_virg = text.find(".")

    if (len(text) - 1) - pos_virg == 0:

        text += "00"

    elif (len(text) - 1) - pos_virg == 1:

        text += "0"

    texto = text.replace(".", ",")

    return f"R${texto}"