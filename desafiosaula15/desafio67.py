print('{}TABUADA V3.0{}'.format('\033[35m', '\033[m'))
numero = contagem = 0
while True:
      numero = int(input('Digite um número para ver a tabuada: '))
      if numero<=0:
        print('O programa foi interrompido, pois o número é {}negativo{} '.format('\033[31m', '\033[m'))
        break
      else:
        for contagem in range(0, 10):
            contagem+=1
            print(f'{numero} x {contagem} = {numero*contagem}')
                     
