import pandas as pd 
import csv
import matplotlib.pyplot as plt
# extração
df = pd.read_csv("arquiv.csv")
print(df['DATACOMUNICACAO'].describe())

# import ipdb; ipdb.set_trace()

# transformação
df = df[['DATAOCORRENCIA', 'DESCR_MARCA_VEICULO']]
df = df.groupby('DESCR_MARCA_VEICULO').size()
plt.bar(df.index, df.values)
plt.title('Roubo de carro por marca')
plt.xlabel('Marca do veículo')
plt.ylabel('Número de roubos')
plt.title('Roubo de carro por marca (2023)')

plt.xlabel('Marca do veículo', size=12)
plt.ylabel('Número de roubos', size=12)
# Alterar a cor das barras
plt.bar(df.index, df.values, color=['red', 'green', 'blue', 'yellow', 'purple', 'black'])
#load
plt.show()
