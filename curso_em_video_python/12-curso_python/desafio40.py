nota1 = float(input('Me fale sua primeira nota: '))
nota2 = float(input('Me fale sua segunda nota: '))
media = (nota1 + nota2)/2
if media<5.0 :
    print('Você foi \033[1;31mREPROVADO\033[0;0m.')
elif media>=5 and media<=6.9 :
    print('Vocẽ está de \033[1;33mRECUPERAÇÃO\033[0;0m.')
elif media >=7 :
    print('Parabéns, você foi \033[1;32mAPROVADO\033[0;0m.')
