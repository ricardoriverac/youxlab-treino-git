while True:
  numero=int(input('Digite um numero e descubra a tabuada!:'))
  if numero < 0:
      break
 
  for i in range (1,11):
     print(f'{numero}*{i}={numero* i}')
    
    