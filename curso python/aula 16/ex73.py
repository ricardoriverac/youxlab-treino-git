tabelaBrasileirao = ('Flamengo', 'Palmeiras', 'Ceará', 'Juventude', 'Fluminense', 'Vasco', 'Internacional', 'Fortaleza','Corinthians', 'Botafogo' , 'Bragantino', 'Cruzeiro', 'Grêmio', 'Bahia', 'São Paulo', 'Atlético-MG', 'Mirassol', 'Santos', 'Vitória', 'Sport')
print("Todos os times e posições")
print ("\t-----" * 10)
for colocacao, nome in enumerate(tabelaBrasileirao):
    print (f"{colocacao+1} --> \033[34mTIME\033[m {nome} ")
print ("\fOs 5 primeiros colocados")
print ("\t-----" * 10)
print (tabelaBrasileirao[0:5]) 
print ("\t-----" * 10)
print ("\fOs 4 últimos colocados")
print ("\t-----" * 10)
print (tabelaBrasileirao[-4:]) 
print ("\t-----" * 10)
print ("\fOs times em ordem alfabética")
print ("\t-----" * 10)
print (sorted(tabelaBrasileirao)) 
print ("\t-----" * 10)
print (f"\fO time fortaleza está na {tabelaBrasileirao.index('Fortaleza')+1}º posição.")
print ("\t-----" * 10)




