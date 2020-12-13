import csv
from numpy import *
import matplotlib.pyplot as plt

if __name__ == "__main__":
    a=array([[0,0],[0,1],[1,0],[1,1]])
    y=array([0,0,0,1])
    Etot=zeros((11,11))
    print(Etot)
    for w1 in range(0,11):
        for w2 in range(0,11):
            E=[]
            Etemp = 0
            for i in range(0,4):
                y=(w1-5)*a[i][0] + (w2-5)*a[i][1]
                t=0
                print("a[" + str(i) + "][0] : " + str(a[i][0]))
                print("a[" + str(i) + "][1] : " + str(a[i][1]))
                if y<=0 :
                    y=0
                else:
                    y=1
                if (a[i][0] == 1 and a[i][1] ==1):
                    t=1
                E.append(0.5*(y-t)*(y-t))
            for k in E:
                Etemp += k
            print("Etemp : " + str(Etemp))
            Etot[w1][w2] = Etemp
            print("w1 : " + str(w1))
            print("w2 : " + str(w2))
            print("Etot[w1][w2] : " + str(Etot[w1][w2]))
    print(Etot)
    plt.imshow(Etot)
    plt.show()