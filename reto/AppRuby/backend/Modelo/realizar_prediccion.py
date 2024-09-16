import numpy as np
import pandas as pd
import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)

# Cargar el modelo entrenado desde el archivo
modelo = joblib.load('Clasificador.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    # Cargar la nueva muestra desde el archivo CSV
    file = request.files['file']
    nueva_muestra = pd.read_csv(file, header=None)

    # Obtener las probabilidades de cada clase
    probabilidades = modelo.predict_proba(nueva_muestra)

    # Construir la respuesta JSON con probabilidades y la clase predicha
    response = {
        "probabilidades": probabilidades[0].tolist(),  # Convertir a lista
        "clase_predicha": modelo.classes_[probabilidades[0].argmax()]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
