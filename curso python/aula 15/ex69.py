continuar = 'S'
contadorMaiorIdade = 0
contadorSexoMasculino = 0
contadorMulherabaixoDe20Anos = 0
while continuar == "S":
    idade = int (input ("Qual sua idade ? "))
    sexo = str (input ("Qual é seu sexo, digite \033[36mF\033[m  para feminino e  \033[36mM\033[m  para masculino] :"))
    continuar = str (input ("Quer continuar [S/N] ? ")).upper()
    if idade >= 18:
        contadorMaiorIdade += 1
    if sexo in "Mm":
       contadorSexoMasculino += 1
    if sexo in "Ff" and idade < 20:
        contadorMulherabaixoDe20Anos += 1
print ("FIIM")
print (f"Quantas pessoas tem mais de 18 anos , {contadorMaiorIdade}")
print (f"Quantidade de homens, {contadorSexoMasculino}")
print (f"Quantas mulheres tem menos de 20 anos, {contadorMulherabaixoDe20Anos}")