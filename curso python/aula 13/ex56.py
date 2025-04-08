NomeHomemMaisVelho = ''
maioridade = 0
somaIdade = 0
mediaIdade = 0
contadorMulherabaixoDe20Anos= 0
for c in range (1,5):
    nome = str (input ("Qual é o seu nome ? "))
    idade = int (input ("Qual é a sua idade ? "))
    sexo = str (input ("Qual é o seu sexo ? "))
    somaIdade += idade
    if c == 1 and sexo in "Mm":
        maioridade = idade
        NomeHomemMaisVelho = nome
    if sexo in "Mm" and idade > maioridade:
        maioridade = idade
        NomeHomemMaisVelho = nome
    if sexo in "Ff" and idade < 20:
        contadorMulherabaixoDe20Anos += 1
mediaIdade = somaIdade / 4
print ("A média da idade do grupo é  \033[33m{}\033[m.".format(mediaIdade))
print ("A idade do homem mais velho é  \033[31m{}\033[m anos, seu nome é  \033[32m{}\033[m.".format(maioridade,NomeHomemMaisVelho))
print ("\033[36m{}\033[m é a quantidade de mulheres com idade inferior a 20. ".format(contadorMulherabaixoDe20Anos))  
  