def ajuda(valor):
    help(valor)



#programa principal
comando = ''
while True:
    valor = str(input('Funções ou Bibliotecas: ')).strip().lower()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(valor)