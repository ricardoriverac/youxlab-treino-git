from time import sleep

def maior(*numeros):
    if len(numeros) == 0:
        print("Nenhum número foi informado.")
        return
    sleep(0.3)
    maior_valor = numeros[0]
    for num in numeros:
        if num > maior_valor:
            maior_valor = num
    
    print(f"Os valores informados foram: {numeros}")
    print(f"O maior valor informado foi: {maior_valor}")

maior(1, 5, 9, 3, 7)
maior(100, 20, 300, 400)
maior()  