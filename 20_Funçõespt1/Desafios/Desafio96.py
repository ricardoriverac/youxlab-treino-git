print('====JOGO DE MATEMÁTICA====')
print('Depois de ter cumprido uma etapa pressione Enter para continuar')
p1 = str(input('Pense em um número.'))
p2 = str(input('Multipliqueo por 2.'))
import random
lista = [2, 4, 6, 8, 10]
lista2 = random.choice(lista)
p3 = str(input('Some {} à conta.'.format(lista2)))
p4 = str(input('Divida por 2'))
p5 = str(input('Menos o número que você pensou...'))
resultado = lista2 / 2
print('O resultado será {}'.format(resultado))