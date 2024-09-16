from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)

modelo = joblib.load('Modelo/Clasificador.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    nueva_muestra = pd.read_csv(file, header=None)

    probabilidades = modelo.predict_proba(nueva_muestra)

    response = {
        "probabilidades": probabilidades[0].tolist(),
        "clase_predicha": modelo.classes_[probabilidades[0].argmax()]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
