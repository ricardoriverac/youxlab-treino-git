#Crie um pacote chamado utilidadesCeV que tenha dois modulos internas chamados
#moeda e dado. Transfira todas as funcionalidades ultlizadas nos desafios anteriores
#para o primeiro pacote e mantenha tudo funcionando

from Exercicios.exe111.ultilidadescev.moeda import moeda

din = int(input("Digite um valor: "))
moeda.resumo(din, "RESUMO DO VALOR", 15, 15)
