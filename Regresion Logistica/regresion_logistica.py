# -*- coding: utf-8 -*-
"""regresion logistica

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wrNzOCGpTDzuEBuGj8GHyQeWBPO-Fd2U
"""

### LIBRERIAS A UTILIZAR ###

#se importan la librerias a utilizar
from sklearn import datasets

### PREPARAR LA DATA ###

#importar los datos de la misma libreria de scikit-learn
dataset = datasets.load_breast_cancer()
print(dataset)

### ENTENDIMIENTO DE LA DATA ###

#verificacion de la informacion contenida en el dataset
print('Infomación en el dataset:')
print(dataset.keys())
print()

#verifico las caracteristicas del dataset
print('Caracteristicas del dataset:')
print(dataset.DESCR)

#seleccionamos todas las columnas
X = dataset.data

#defino los datos correspondientes a las etiquetas
y = dataset.target

### IMPLEMENTACION DE REGRESION LOGISTICA ###

from sklearn.model_selection import train_test_split

#separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#se escalan todos los datos
from sklearn.preprocessing import StandardScaler
escalar = StandardScaler()
X_train = escalar.fit_transform(X_train)
X_test = escalar.transform(X_test)

#defino el algoritmo a utilizar
from sklearn.linear_model import LogisticRegression

algoritmo = LogisticRegression()

#entreno el modelo
algoritmo.fit(X_train, y_train)

#realizacion para la prediccion
y_pred = algoritmo.predict(X_test)

#verificar la matriz de confusión
from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(y_test, y_pred)
print('Matriz de Confusión:')
print(matriz)

#calculo la precisión del modelo
from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred)
print('Precisión del modelo:')
print(precision)

#calcular la exactitud del modelo
from sklearn.metrics import accuracy_score

exactitud = accuracy_score(y_test, y_pred)
print('Exactitud del modelo:')
print(exactitud)

#calculo de la sensibilidad del modelo
from sklearn.metrics import recall_score

sensibilidad = recall_score(y_test, y_pred)
print('Sensibilidad del modelo:')
print(sensibilidad)

#calculo del puntaje F1 del modelo
from sklearn.metrics import f1_score

puntajef1 = f1_score(y_test, y_pred)
print('Puntaje F1 del modelo:')
print(puntajef1)

#calculo de la curva ROC - AUC del modelo
from sklearn.metrics import roc_auc_score

roc_auc = roc_auc_score(y_test, y_pred)
print('Curva ROC - AUC del modelo:')
print(roc_auc)

print('precisión del modelo:', precision)
print('exactitud del modelo:', exactitud)
print('sensibilidad del modelo:', sensibilidad)
print('puntaje f1 del modelo:', puntajef1)
print('curva roc - auc del modelo:', roc_auc)