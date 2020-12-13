from Character import Character
from Army import Army
import csv
from numpy import *

if __name__ == "__main__":
    #test = Character("Sylvain","Sylvain", 666, "Archer", 50)
    #print(test)
    #test.setAge(56)
    #print(test)
    characterList = []
    armyList = []
    ArmiesTotalMoral = 0
    characterMoral = zeros(5)
    armyMoral = zeros(5)
    with open('characters.csv', newline='') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in fileReader:
            if fileReader.line_num > 1:
                characterList.append(Character(row[0],row[1],row[2],row[3],row[4]))
    for c in characterList:
        print(c)
        armyList.append(Army(c,random.randint(20,100)))
        
    for a in armyList:
        print(a)
        ArmiesTotalMoral = ArmiesTotalMoral + a.get_total_moral()
    
    print(ArmiesTotalMoral)

    for i in range(5):
        characterMoral[i] = characterList[i].getboostMoral()
        armyMoral[i] = armyList[i].get_Moral()

    print(characterMoral)
    print(armyMoral)