sexo = str (input ("Digite seu sexo , M para mascuino e F para feminino: ")).strip().upper()[0]
while sexo not in 'FfMm':
    print ("Sexo inválido!")
    sexo = str (input("Digite novamente seu sexo , M para mascuino e F para feminino:")).strip().upper()[0]
print ("Sexo  \033[33m{}\033[m válidado com sucesso!".format(sexo))