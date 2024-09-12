import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
data = pd.read_csv('../dataset/processed_insurance.csv')

# Distribuição das variáveis
sns.histplot(data['charges'], kde=True)
plt.title('Distribuição dos Encargos do Seguro')
plt.savefig('../results/visualizations/distribution_plot.png')

# Correlação entre variáveis
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Mapa de Correlação')
plt.savefig('../results/visualizations/correlation_heatmap.png')

# Análise adicional conforme necessário
# ...

print("Análise exploratória concluída. Resultados salvos em 'results/visualizations/'.")
