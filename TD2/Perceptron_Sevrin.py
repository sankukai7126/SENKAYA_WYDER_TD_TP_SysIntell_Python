from random import *
import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self,nbInputs,epochs,learningRate):
        self.nbInputs = nbInputs # 3 avec le biais
        self.epochs = epochs
        self.learningRate = learningRate # 0.01 je crois
        #self.biais = 1
        self.w = np.zeros(nbInputs)
        
    #On predit le resultat des deux entrées
    def predict(self,a0,a1,a2):
        p = self.w[0]*1 + self.w[1]*a1 + self.w[2]*a2
        if p <= 0:
            return 0
        else:
            return 1

    def train(self,inputs,outputs):
        for k in range(0,self.epochs,1):
            for i in range(0,len(inputs),1):
                prediction = self.predict(inputs[i][0],inputs[i][1], inputs[i][2])
                t=outputs[i]
                erreur = 0.5*((prediction-t)**2)
             
                #on ajuste les valeurs
                for indexPoids in range(1,self.nbInputs,1):
                    self.w[indexPoids] = self.w[indexPoids] + self.learningRate * ( outputs[i] - prediction ) * inputs[i][indexPoids]

                self.w[0] = self.w[0] + self.learningRate * ( outputs[i] - prediction  )

                print("iteration n" + str(k) + " prediction:" + str(prediction) + " erreur:" + str(erreur) + " biais :" + str(self.w[0]) + "  a1 :" + str(self.w[1]) + "  a2 :" + str(self.w[2])) #pour afficher les valeurs
        f= open("C:/Users/Mikrail/Documents/4A IA/TD/Projet/TD2/file.csv","w")
        f.write(str(self.w[0]) + "\n" + str(self.w[1]) + "\n" + str(self.w[2]))
        f.close()

    def loadValue(self):
        f= open("C:/Users/Mikrail/Documents/4A IA/TD/Projet/TD2/file.csv","r")
        a = f.readlines()
        self.w[0] = a[0]
        self.w[1] = a[1]
        self.w[2] = a[2]
        f.close()
                 
