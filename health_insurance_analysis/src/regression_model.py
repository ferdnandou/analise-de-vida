import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Carregar dados
data = pd.read_csv('../dataset/processed_insurance.csv')
X = data.drop('charges', axis=1)
y = data['charges']

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Previsões e avaliação
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

with open('../results/model/model_performance.txt', 'w') as f:
    f.write(f'Mean Squared Error: {mse}\nR^2 Score: {r2}\n')

# Resumo do modelo
with open('../results/model/model_summary.txt', 'w') as f:
    f.write(f'Coeficientes: {model.coef_}\nIntercepto: {model.intercept_}\n')

print("Modelagem estatística concluída. Resultados salvos em 'results/model/'.")
