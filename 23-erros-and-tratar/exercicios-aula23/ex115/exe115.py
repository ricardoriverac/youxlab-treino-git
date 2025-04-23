from lib import interface
from lib import arquivo

arq = 'teste.txt'
if not arquivo.arquivoexiste(arq):
    arquivo.criaraarquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoas cadastradas' , 'Cadastrar pessoa' , 'Sair do sistema'])
    if resposta == 1:
        arquivo.lerarquivo(arq)
    elif resposta == 2:
        interface.cabecalho('NOVO CADASTRATO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        arquivo.novocadastro(arq , nome , idade)
    elif resposta == 3:
        interface.cabecalho('  \033[36mSAINDO DO SISTEMA... ATÉ LOGO\033[m')
        break
    else:
        print('\033[31mERRO>OPÇÃO INVALIDA\033[m')
    interface.stop(1)






#programa principal
# while True:
#         texto('MENU PRINCIPAL')
#         print('1 - Ver pessoas cadastradas')
#         print('2 - Cadastrar uma pessoa')
#         print('3 - Sair')
#         while True:
#             try:
#                 opcao = int(input('Sua opção: '))
#             except ValueError:
#                 print('\033[31mERRO: Digite um número válido\033[m')
#             else:
#                 break
#         if opcao == 1 :
#             texto('OPÇÃO 1')
#         if opcao == 2 :
#             texto('OPÇÃO 2')
#         if opcao == 3 :
#             texto('SAINDO DO SISTEMA... ATÉ LOGO')
#             break
#         if opcao > 3:
#             print('\033[31mERRO: Digite uma opção válida\033[m')
#             continue
