import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.cross_validation import train_test_split #en otra version de sklearn puede ser from sklearn.module_selection import train_test_split
from sklearn import preprocessing

#iris setosa = 0
#iris versicolor = 1
#iris virginica = 2  
iris = pd.read_csv('iris.csv')
X = preprocessing.scale(iris.drop('Species', axis=1)) #estandarizamos la data (media 0 y desv. est. 1)
Y = to_categorical(iris['Species']) #convierte a categorica la data numerica p.e. [0., 1., 0.]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.8) #crea 4 arrays partiendo de X, y Y separando como test data al 30% del total (0.3)

#Creamos la red neuronal 
model = Sequential()
model.add(Dense(12, input_dim = 4, activation = 'relu'))
model.add(Dense(3, activation='softmax'))

#Compilamos el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])
#categorical_crossentropy es la loss function que se usa en multiclass classification

#Entrenamos el modelo
model.fit(X_train, Y_train, epochs = 200, batch_size=10)

#Testeamos el modelo 
test_loss, test_accuracy = model.evaluate(X_test, Y_test)






