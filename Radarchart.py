# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import random

resposta = [0, ]
i = 1
while i < 25:
    nota = random.randint(0, 10)
    resposta.append(nota)
    print("nota",i," :",nota)
    i=i+1

Lideranca = [(resposta[9] + resposta[13] + resposta[15]) / 3]
Estrategia = [(resposta[1] + resposta[6] + resposta[17]) / 3]
Relacionamento = [(resposta[15] + resposta[19] + resposta[21]) / 3]
Cultura = [(resposta[3] + resposta[7] + resposta[22]) / 3]
Pessoas = [(resposta[4] + resposta[14] + resposta[23]) / 3]
Estrutura = [(resposta[2] + resposta[5] + resposta[8]) / 3]
Processo = [(resposta[11] + resposta[18] + resposta[20]) / 3]
Fundig = [(resposta[10] + resposta[12] + resposta[24]) / 3]


# Set data
df = pd.DataFrame({
    'group': ['A'],
    'Liderança': [Lideranca],
    'Estratégia': [Estrategia],
    'Relacionamento': [Relacionamento],
    'Cultura': [Cultura],
    'Pessoas': [Pessoas],
    'Estruturas': [Estrutura],
    'Processo': [Processo],
    'Funding': [Fundig]

})

# number of variable
categories = list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='k', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 9], ["2", " 4", "6", "8"], color="grey", size=7)
plt.ylim(0, 10)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=1)

plt.show()
