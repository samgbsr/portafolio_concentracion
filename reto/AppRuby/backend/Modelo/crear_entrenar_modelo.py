import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Cargar los datos desde el archivo CSV
data_train = pd.read_csv('mitbih_train.csv', header=None)
data_test = pd.read_csv('mitbih_test.csv', header=None)

# Separar las características (X) y las etiquetas (y)
X_train = data_train.iloc[:, :-1]  # Todas las columnas excepto la ultima son características
y_train = data_train.iloc[:, -1]   # La ultima columna es la categoría

X_test = data_test.iloc[:, :-1]  # Todas las columnas excepto la ultima son características
y_test = data_test.iloc[:, -1]   # La ultima columna es la categoría

# Crear un modelo SVC
model = SVC(class_weight='balanced', probability=True)

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Guardar el modelo entrenado
joblib.dump(model, 'Clasificador.pkl')

# Evaluar el modelo
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Calcular la tabla de confusión normalizada
conf_matrix = confusion_matrix(y_test, y_pred, normalize='true')

# Desplegar la tabla de confusión normalizada usando seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt=".2f", cmap="Blues", cbar=False)
plt.title("Normalized Confusion Matrix")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.show()
