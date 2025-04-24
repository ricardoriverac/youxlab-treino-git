num= [9,2,3,4,7]
num [2]= 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 4 in num:
    num.remove(5)
else:
    print("Nao achei o numero 4.")
num.remove(2)
print(num)
print(f"Essa lista  tem {len(num)} elementos.")