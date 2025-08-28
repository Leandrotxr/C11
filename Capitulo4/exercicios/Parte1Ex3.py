import random

import numpy as np

mtz = np.zeros((2,2), dtype=int)
linha = random.randint(0,1)
coluna = random.randint(0,1)
mtz[linha][coluna] = 1

tentativas = 1
achou = False

while tentativas < mtz.size and not achou:
    print("\nJogada", tentativas)
    lin = int(input("Digite a linha (0 ou 1): "))
    col = int(input("Digite a coluna (0 ou 1): "))

    if mtz[lin,col] == 1:
        print("Game Over! :( Try Again!")
        achou = True
    else:
        tentativas += 1

if not achou:
    print("Congratulations! You beat the game! :)")