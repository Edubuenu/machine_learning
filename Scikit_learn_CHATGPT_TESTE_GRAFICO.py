import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Gerando dados de exemplo
X, y = make_classification(n_samples=1000, n_features=5, random_state=42)

# Dividindo os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo de regressão logística
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Fazendo previsões com o modelo treinado
y_pred = lr.predict(X_test)

# Calculando a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)

# Calculando a matriz de confusão
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusão:\n", conf_matrix)

# Plotando o gráfico
plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
plt.title("Distribuição dos dados")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
