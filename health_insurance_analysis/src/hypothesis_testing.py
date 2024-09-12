import pandas as pd
from scipy import stats

# Carregar dados
data = pd.read_csv('../dataset/processed_insurance.csv')

# Teste de diferença entre fumantes e não fumantes
smokers = data[data['smoker'] == 1]['charges']
non_smokers = data[data['smoker'] == 0]['charges']
t_stat, p_value = stats.ttest_ind(smokers, non_smokers)

with open('../results/statistical_tests/smoker_test_results.txt', 'w') as f:
    f.write(f'T-statistic: {t_stat}\nP-value: {p_value}\n')

# Teste de diferença entre homens e mulheres
# ...

print("Testes estatísticos concluídos. Resultados salvos em 'results/statistical_tests/'.")
