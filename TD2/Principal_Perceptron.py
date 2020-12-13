import csv
from numpy import *
import matplotlib.pyplot as plt
#from Perceptron import * 
from Perceptron_Sevrin import *

if __name__ == "__main__":
    a=array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
    y=array([0,0,0,1])
    P=Perceptron(3,20,0.01)
    #P.train(a,y)
    P.loadValue()
    print(P.predict(1,0,0))
    print(P.predict(1,0,1))
    print(P.predict(1,1,0))
    print(P.predict(1,1,1))