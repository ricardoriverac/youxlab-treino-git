import time
import emoji

n=int(input("Digite um número para contagem regreciva: \n"))
for c in range (n, 0, -1):
    print(c)
    time.sleep(1)
print("BUM, BUMM, POW!!")