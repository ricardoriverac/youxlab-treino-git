# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome 
# e idade em um arquivo de texto simples.

# O sistema so vai ter 2 opçoes: cadastrar uma nova pessoa e listar
# todas as pessoas cadastradas.

import interface
import dados

while True:
    opc = interface.menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])

    if opc == 1:
        interface.cabecalho("PESSOAS CADASTRADAS")
        dados.listar_pessoas()

    elif opc == 2:
        interface.cabecalho("NOVO CADASTRO")
        nome = input("Nome: ").strip()
        while True:
            try:
                idade = int(input("Idade: "))
                break
            except ValueError:
                print("Por favor, digite uma idade válida.")
        dados.cadastrar_pessoa(nome, idade)

    elif opc == 3:
        interface.cabecalho("Saindo do sistema... Até logo!")
        break

