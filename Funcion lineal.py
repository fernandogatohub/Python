import numpy as np
import pandas as pd
from keras.models import Sequential #permite aÃ±adir layers
from keras.layers import Dense
from matplotlib import pyplot as plt #para hacer los graficos

model=Sequential() #En keras hay dos tipos de modelos: sequenctial y class
#añadimos el imput layer. Dense es el tipo de layer en el que cada input esta conectado con cada output a través de un weight(10 neuronas, imput_dim = 1 dimension en el input layer (una sola columna), funcion de activacion relu)
model.add(Dense(10, input_dim=1, activation = 'relu')) 
#añadimos el primer hidden layer
model.add(Dense(30,activation = 'relu'))
#añadimos el segundo hidden layer
model.add(Dense(30,activation = 'relu'))
#añadimos el output layer
model.add(Dense(1,activation = 'linear'))

#Ahora toca compilar que es como configurar el proceso de aprendizaje
model.compile(loss='mse', optimizer='adam') #loss es la función que queremos minimizar. mse es Mean Square Value. Optimizer es el algoritmo que se utilizará para minimizar la función loss.

#Entrenamos a la red con el dataset para entrenar
train_dataset = pd.read_csv('Dataset_fl_train_posi_y_nega.csv')
x = train_dataset['X']
y = train_dataset['Y']
model.fit(x,y,epochs=1000)

#Testeamos el modelo entrenado
test_dataset = pd.read_csv('Dataset_fl_test.csv')
x_test = test_dataset['X']
y_predicted = model.predict(x_test)

#Ploteamos
plt.scatter(x,y)
plt.scatter(x_test,y_predicted)