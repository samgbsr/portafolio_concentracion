import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras import backend as K
import pickle

# Load data
inputFile = open('biomas.obj', 'rb')
data = pickle.load(inputFile)

processed_images = data['Images']
labels = data['Labels']

# Preparar los datos
x = np.array(processed_images)
x = x.reshape(x.shape[0], x.shape[1], x.shape[2], 1)
x = x / 255.0

y = np.array(labels, dtype=int)
yc = to_categorical(y)

img_rows, img_cols = x.shape[1], x.shape[2]
num_classes = yc.shape[1]

# Número de particiones para la validación cruzada
n_splits = 5
kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

# Número de épocas
epochs = 100

# Lista para guardar las exactitudes
accuracies = []

# Función para construir el modelo
def build_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(img_rows, img_cols, 1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
    return model

# Ejecutar validación cruzada
for fold, (train_index, val_index) in enumerate(kf.split(x), 1):
    print(f'Fold {fold}/{n_splits}')
    x_train, x_val = x[train_index], x[val_index]
    y_train, y_val = yc[train_index], yc[val_index]

    model = build_model()
    history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=epochs, batch_size=128, verbose=1)

    # Evaluar el modelo
    val_loss, val_accuracy = model.evaluate(x_val, y_val, verbose=0)
    accuracies.append(val_accuracy)

    # Limpiar sesión de Keras para liberar memoria
    K.clear_session()

# Calcular el promedio de las exactitudes
mean_accuracy = np.mean(accuracies)
print(f'Promedio de exactitud: {mean_accuracy:.4f}')
