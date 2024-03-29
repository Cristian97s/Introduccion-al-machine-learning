# -*- coding: utf-8 -*-
"""Regresion lineal multiple

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1av58ck2SjqaS75ZGaTDLlZ2rVg2cogER
"""

### Librerias a utilizar ###

#se importan la librerias a utilizar
from sklearn import datasets, linear_model

#importamos lo datos de la misma libreria de scikt-learn
boston = datasets.load_boston()
print(boston)
print()

### ENTENDIMIENTO DE LA DATA ###

#verifico la informacion contenida en el dataset
print('Informacion en el dataset:')
print(boston.keys())
print()

#verifico las caracteristicas del dataset
print('Caracteristicas del dataset:')
print(boston.DESCR)

#verifico la cantidad de datos que hay en los dataset
print('cantidad de datos:')
print(boston.data.shape)
print()

#verifico la informacion de las columnas
print('Nombre columnas')
print(boston.feature_names)

### PREPARAR LA DATA REGRESION LINEAL MULTIPLE ###

#seleccion de las columnas 5, 6 y 7 del dataset
X_multiple = boston.data[:, 5:8]
print(X_multiple)

#defino los datos correspondientes a las etiquetas
y_multiple = boston.target

### IMPLEMENTACION DE REGRESION LINEAL MULTIPLE ###

from sklearn.model_selection import train_test_split

#separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

#definir el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

#entrenando el modelo
lr_multiple.fit(X_train, y_train)

#realizo una predicion
Y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO REGRESION LINEAL MULTIPLE')
print()
print('Valor de las pendientes o coeficientoes "a":')
print(lr_multiple.coef_)

print('valor de la interseccion o coeficiente "b":')
print(lr_multiple.intercept_)

print('precision del modelo:')
print(lr_multiple.score(X_train, y_train))