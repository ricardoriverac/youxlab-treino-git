# Ideia do joão: Jogo de roleta russa.

import random
from time import sleep

slotDaMunicao = random.randint(0, 6) 

for m in range(6):
    print("\nSorteando quem irá apertar.\n")
    sleep(2)
    sortearJogador = random.randint(0, 1)

    if sortearJogador == 1:
        print("\nJogador sorteado.\n")
        sleep(1)
        jogador = input("Aperte o gatilho: ").strip().lower()

        # if jogador == "apertar":
        #     jogador = random.randint(0, 6)
        #     print(f"O jogador apertou o gatilho")
        #     sleep(1)

        if m == slotDaMunicao:
            sleep(1)
            print("Jogador morreu.")
            break
    else:
        print("\nComputador sorteado.\n")
        sleep(1)
        # computador = random.randint(0, 6)
        print(f"O computador apertou o gatilho")
        sleep(1)
        if m == slotDaMunicao:
                sleep(1)
                print("Computador morreu.")
                break
    sleep(1)
            


    
