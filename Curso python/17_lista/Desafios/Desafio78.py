listanum = []
mai =0
men = 0
for c  in range (0, 5):
    listanum.append(int(input(f"Digite um valor na posição {c}:")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c]>mai:
            mai = listanum[c]
        if listanum[c]<men:
            men = listanum[c]
print("====="*8)
print(f"Voce digitou {listanum}")
print(f"O maior numero digitado foi {mai}")
print(f"o menor numero digitado foi {men}")
