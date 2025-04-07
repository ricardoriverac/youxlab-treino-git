adição = 0
cnt = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        adição += c
        cnt += 1
print(' o total de {} valores digitados foi {}'.format(cnt, adição))
