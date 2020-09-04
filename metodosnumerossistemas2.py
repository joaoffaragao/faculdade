import numpy as np            # Importa módulo numpy para criação das matrizes e vetores
from scipy import linalg      # Importa linalg de scipy para solução sistemas de equações lineares

A = np.array([[1,0,0,10], [-1,1,0,4], [0,-1,1,5], [0,0,-1,6]])   # Cria a matriz A
print("matriz A", A)

angulo = ((75*np.pi)/180)
g = 9.82
m =[10,4,5,6]
u =[0.25,0.3,0.2]
b=[]
i=0

while len(m) > i:
    if i<len(u):
      vetorb = m[i]*g*(np.sin(angulo)-u[i]*np.cos(angulo))
      b.append(vetorb)
    else:
        vetorb =m[i]*g
        b.append(vetorb)
    i = i + 1
vb = np.array([b])
vm = np.array([m])
vu = np.array([u])

print("matriz B", vb)
print("matriz m", vm)
print("matriz u", vu)


x = linalg.solve(A, b)                  #    Resolve o sistema utilizando linalg.solve
print('x = ', x)