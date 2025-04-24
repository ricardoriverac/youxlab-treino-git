from time import sleep
import defs as d

cadastro = {}

d.titulo('CADASTRO DE CONTA DO LAB')
while True:
    cadastro.clear()

    cadastro['gmail'] = input('Registre seu e-mail: ')
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
            d.lin()
            sleep(2)
           
            break
    else:
        print('SUA SENHA TEM QUE SER DE 4 DÍGITOS!!')
        d.lin()
logar = str(input('Deseja fazer o login na sua conta [s/n]? ')).lower()[0]

if logar == 's':
    while True:
        loginEmail = str(input('E-mail: '))
        if loginEmail != cadastro['gmail']:
            print('Email não cadastrado, tente novamente.')
        else:
            loginSenha = int(input('Senha (Esqueceu a senha? Se sim digite 999.): '))
            if loginSenha == cadastro['senha']:
                d.lin()
                print('CONTA LOGADA, AGORA VOCÊ PODE DESFRUTAR DE TODOS NOSSOS RECURSOS, APROVEITE!!')
                print()
                break
            elif loginSenha == 999:
                while True:
                    del cadastro['senha']
                    cadastro['senha'] = int(input('Digite sua nova senha: '))
                    sleep(2)
                    confirm = int(input('Confirme a senha: '))
                    if confirm != cadastro['senha']:
                        print('As senhas não coincidem. Tente novamente.')
                    else:
                        print('Senha alterada com sucesso!')
                        break
                break
            else:
                print('Senha incorreta! Tente novamente.')
    sleep(3)
    print()
    d.titulo('MENU')
    print('''    [ 1 ] Consultar dados
    [ 2 ] Trocar de conta
    [ 3 ] Sair
''')
    opcao = int(input('Opção: '))
    while True:
        if opcao == 1:
            d.lin()
            print(f'E-mail: {cadastro["gmail"]}')
            print(f'Senha: {cadastro["senha"]}')
            d.lin()
        elif opcao == 3:
            print('Finalizando menu...')
            break
else:   
    print('Obrigado por se cadastrar no nosso site! Quando quiser você pode fazer o login para aproveitar nossos recursos.')




# cadastro = {}

# d.titulo('CADASTRO DE CONTA DO LAB')
# while True:
#     cadastro.clear()
#     cadastro['senha'] = int(input('Registre sua senha de 4 dígitos: '))    
#     d.lin()
#     if cadastro['senha'] <= 9999:
#         confirm = int(input('Confirme sua senha: '))
#         d.lin()
#         if confirm != cadastro['senha']:
#             print('As senhas não correspondem, tente novamente.')
#             d.lin()
#         else:    
#             print('Registrando senha...')
#             sleep(3)
#             d.lin()
#             print('SENHA REGISTRADA!!')
#             d.lin()
#             sleep(2)
#             d.lina('~')
#             break
#     else:
#         print('SUA SENHA TEM QUE SER DE 4 DÍGITOS!!')
#         d.lin()
# logar = str(input('Deseja fazer o login na sua conta [s/n]? ')).lower()[0]
# if logar == 's':
#     while True:
#         login = int(input('Senha (Esqueceu a senha? Se sim digite 999.): '))
#         if login == cadastro['senha']:
#             d.lin()
#             print('CONTA LOGADA, AGORA VOCÊ PODE DESFRUTAR DE TODOS NOSSOS RECURSOS, APROVEITE!!')
#             print()
#             break
#         elif login == 999:
#             while True:
#                 del cadastro['senha']
#                 cadastro['senha'] = int(input('Digite sua nova senha: '))
#                 sleep(2)
#                 confirm = int(input('Confirme a senha: '))
#                 if confirm != cadastro['senha']:
#                     print('As senhas não coincidem. Tente novamente.')
#                 else:
#                     print('Senha alterada com sucesso!')
#                     break
#             break
#         else:
#             print('Senha incorreta! Tente novamente.')
#     sleep(3)
#     print()
#     d.titulo('MENU')
#     print('''    [ 1 ] Consultar dados
#     [ 2 ] Trocar de conta
#     [ 3 ] Sair
# ''')
#     opcao = int(input('Opção: '))
#     if opcao == 1:
#         for k in (cadastro):
#             print(f'Senha: {k}')
# else:
#     print('Obrigado por se cadastrar no nosso site! Quando quiser você pode fazer o login para aproveitar nossos recursos.')