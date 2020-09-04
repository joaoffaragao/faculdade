import numpy as np            # Importa módulo numpy para criação das matrizes e vetores
from scipy import linalg      # Importa linalg de scipy para solução sistemas de equações lineares

A = np.array([[70,1,0],[60,-1,1],[40,0,-1]])   # Cria a matriz A
print(A)

b = np.array([[636], [518], [307]])            # Cria o vetor b
print(b)

x = linalg.solve(A, b)                      # Resolve o sistema utilizando linalg.solve
print('x = ',x)