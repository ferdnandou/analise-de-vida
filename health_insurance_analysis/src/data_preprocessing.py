import pandas as pd

# Carregar dados
data = pd.read_csv('../dataset/insurance.csv')

# Pré-processamento
# Exemplo: tratamento de valores ausentes, codificação de variáveis categóricas, etc.
data['sex'] = data['sex'].map({'male': 0, 'female': 1})
data['smoker'] = data['smoker'].map({'yes': 1, 'no': 0})
data = pd.get_dummies(data, columns=['region'], drop_first=True)

# Salvar dados pré-processados
data.to_csv('../dataset/processed_insurance.csv', index=False)
print("Dados pré-processados salvos em 'dataset/processed_insurance.csv'.")
