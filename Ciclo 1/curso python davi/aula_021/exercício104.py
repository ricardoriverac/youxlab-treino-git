def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
num = leiaInt("Digite um número inteiro: ")
print(f"\033[32mVocê acabou de digitar o número {num} corretamente\033[32m.")