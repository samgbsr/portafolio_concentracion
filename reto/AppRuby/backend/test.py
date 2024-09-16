import requests

csv_file = {'file': open('./Modelo/Muestras/Muestra_cat1.csv', 'rb')}

response = requests.post('http://localhost:5000/predict', files=csv_file)

print(response.json())
