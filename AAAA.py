import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Criar um DataFrame
data = {'x': np.arange(10), 'y': np.random.rand(10)}
df = pd.DataFrame(data)

# Plotar os dados
plt.scatter(df['x'], df['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Dispersão')
plt.show()

