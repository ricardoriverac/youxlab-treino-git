import time

def digitar(texto, delay=0.05, end='\n'):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

digitar('\033[1;34m-=-=-=-=-= Jogo do Par ou Ímpar =-=-=-=-=-\033[m', end='')




