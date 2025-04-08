contadorHomemMaisVelho = 0
contadorMulherabaixoDe20Anos= 0
for c in range (1,5):
    nome = str (input ("Qual é o seu nome ? "))
    idade = int (input ("Qual é a sua idade ? "))
    sexo = str (input ("Qual é o seu sexo ? "))
    media = (c + idade) / 2
print ("a média foi: {}".format(media))
if sexo == 'masculino' or sexo == 'm' or sexo == 'M':
         contadorHomemMaisVelho = c < idade-1
         print ("{} é o nome do homem mais velho!".format(nome))
elif sexo == 'feminino' or sexo == 'f' or sexo == 'F':
         contadorMulherabaixoDe20Anos = idade < 20 + 1
         print ("{} quantidade de mulheres com idade menor que 20.".format(contadorMulherabaixoDe20Anos))