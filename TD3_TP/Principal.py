import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras import utils
from numpy import *
import matplotlib.pyplot as plt
#test github

inputs = zeros((10,7))
outputs = zeros((10,10))

def save():
    f= open("C:/Users/Mikrail/Documents/4A IA/TD/Projet/TD3/inputs.csv","w")
    for i in range(0,len(inputs)):
        for j in range(0, len(inputs[i])):
            f.write(str(inputs[i][j]) + " ")
        f.write("\n")
    f.close()

    f= open("C:/Users/Mikrail/Documents/4A IA/TD/Projet/TD3/teacher.csv","w")
    for i in range(0,len(outputs)):
        for j in range(0, len(outputs[i])):
            f.write(str(outputs[i][j])  + " ")
        f.write("\n")
    f.close()

if __name__ == "__main__":

    inputs[0] = [1,1,1,1,1,1,0]
    inputs[1] = [0,1,1,0,0,0,0]
    inputs[2] = [1,1,0,1,1,0,0]
    inputs[3] = [1,1,1,1,0,0,1]
    inputs[4] = [0,1,1,0,0,1,1]
    inputs[5] = [1,0,1,1,0,1,1]
    inputs[6] = [1,0,1,1,1,1,0]
    inputs[7] = [1,1,1,0,0,0,0]
    inputs[8] = [1,1,1,1,1,1,1]
    inputs[9] = [1,1,1,1,0,1,1]

    outputs[0] = [1,0,0,0,0,0,0,0,0,0]
    outputs[1] = [0,1,0,0,0,0,0,0,0,0]
    outputs[2] = [0,0,1,0,0,0,0,0,0,0]
    outputs[3] = [0,0,0,1,0,0,0,0,0,0]
    outputs[4] = [0,0,0,0,1,0,0,0,0,0]
    outputs[5] = [0,0,0,0,0,1,0,0,0,0]
    outputs[6] = [0,0,0,0,0,0,1,0,0,0]
    outputs[7] = [0,0,0,0,0,0,0,1,0,0]
    outputs[8] = [0,0,0,0,0,0,0,0,1,0]
    outputs[9] = [0,0,0,0,0,0,0,0,0,1]

    print(inputs)
    print("\n" + "-----------------" + "\n")
    print(outputs)
    print("\n" + "-----------------" + "\n")
    
    save()

    inputs = reshape(inputs,(10,1,7))
    outputs = reshape(outputs,(10,1,10))

    print(inputs)
    print("\n" + "-----------------" + "\n")
    print(outputs)
    print("\n" + "-----------------" + "\n")

    sgd = SGD(lr=0.1) 
    model = Sequential()
    model.add(Dense(10, input_dim = 7, activation='relu'))
    model.add(Dense(64, input_dim = 10, activation='relu'))
    model.add(Dense(64, input_dim = 64, activation='relu'))
    model.add(Dense(10, input_dim = 64, activation='softmax'))
    #   J'affiche une représentation du modèle
    model.summary()
    #   Je compile le modèle avec la descente du gradient et une losse de type (t-y)² (celle vu en cours)
    model.compile(optimizer=sgd, loss='categorical_crossentropy')#'binary_crossentropy')
    #   Je lance l'apprentissage du modèle sur 5000 epochs
    model.fit(inputs, outputs, epochs=5000)
    prediction = model.predict(inputs)
    print(prediction)
    print(model.predict([[[1,1,1,1,0,0,0]]]))
    
