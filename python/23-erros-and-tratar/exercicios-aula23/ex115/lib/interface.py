def leiaint(msg):
        while True:
            try:
                leia = int(input(msg))
            except (ValueError , AttributeError , TypeError):
                print('\033[31mERRO: Digite o número inteiro válido! TENTE NOVAMENTE...\033[m')
                continue
            except KeyboardInterrupt:
                print('\n\033[31mO usuário optou por interromper a opção\033[m')
                break
            else:
                return leia
def linha(tam=42):
    return '-' * tam
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    opc = leiaint('Sua Opção: ')
    return opc
def stop(num):
    from time import sleep
    sleep(num)
    return num
    
