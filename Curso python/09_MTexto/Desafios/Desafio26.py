n1 = str(input("Insira uma frase: "))
n= n1.count("a")
p= n1[0]
u= n1[len(n1)-1]
print("A letra A aparece {}, vezes na frase. ".format(n))
print("A primeira letra e {}".format(p))
print("A ultima letra e {}".format(u))
