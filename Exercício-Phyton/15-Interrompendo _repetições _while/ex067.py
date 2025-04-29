while True:

    numerador = int(input("Qual o número quer multiplicar?: ")) 
    if numerador < 0:
       

       break
    
    for c in range(1, 11):
        print(f'{numerador} x {c}  = {numerador*c}')

   

