#orgulhosa de mim por ter chegado aqui!!! 
idadeMedia= 0
contador= 0
soma= 0
nomeHomemMaisVelho= ''
idadeHomemMaisVelho= 0
mulheresMenosDeVinte= 0
for a in range(1, 5):
    nome= input('Informe o seu nome: ')
    idade= int(input('Agora a sua idade: '))
    sexo= input('E por último, seu sexo: ').upper() .capitalize() [0]
    contador += 1
    soma += idade
    idadeMedia= soma / contador
    if a == 1 and sexo == 'M':
        nomeHomemMaisVelho= nome
        idadeHomemMaisVelho= idade
    else:
        if idade > idadeHomemMaisVelho and sexo == 'M':
            nomeHomemMaisVelho= nome
            idadeHomemMaisVelho= idade
    if sexo == 'F' and idade < 20:
        mulheresMenosDeVinte += 1


