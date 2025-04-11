import time

def digitar(texto, delay=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()