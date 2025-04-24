from time import sleep
import defs as d

cadastro = {}

d.titulo('CADASTRO DE CONTA DO LAB')
while True:
    cadastro.clear()
    cadastro['senha'] = int(input('Registre sua senha de 4 dígitos: '))    
    d.lin()
    if cadastro['senha'] <= 9999:
        confirm = int(input('Confirme sua senha: '))
        d.lin()
        if confirm != cadastro['senha']:
            print('As senhas não correspondem, tente novamente.')
            d.lin()
        else:    
            print('Registrando senha...')
            sleep(3)
            d.lin()
            print('SENHA REGISTRADA!!')
            d.lina('~')
            sleep(2)
            break
    else:
        print('SUA SENHA TEM QUE SER DE 4 DÍGITOS!!')
        d.lin()
logar = str(input('Deseja fazer o login na sua conta [s/n]? ')).lower()[0]
if logar == 's':
    while True:
        login = int(input('Senha: '))
        if login == cadastro['senha']:
            d.lin()
            print('CONTA LOGADA, AGORA VOCÊ PODE DESFRUTAR DE TODOS NOSSOS RECURSOSS, APROVEITE!!')
            print()
            break
        else:
            print('Senha incorreta! Tente novamente.')
else:
    print('Obrigado por se cadastrar no nosso site! Quando quiser você pode fazer o login para aproveitar nossos recursos.')