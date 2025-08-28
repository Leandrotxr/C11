import random

import numpy as np

linha = random.randint(1,11)
coluna = random.randint(1,11)

mtz = np.random.randint(1,101,[linha,coluna])

total_elementos = linha*coluna

if total_elementos % 2 == 0:
    print("A matriz pode virar um vetor 1D com quantidade PAR de elementos.")
else:
    print("A matriz pode virar um vetor 1D com quantidade IMPAR de elementos.")