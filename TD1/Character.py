class Character:
    def __init__(self, nom, prenom, age, profession, boostMoral):
        self.nom = nom
        self.prenom = prenom
        self.age = int(age)
        self.profession = profession
        self.boostMoral = float(boostMoral)

    def getNom(self):
        return self.nom
    
    def getPrenom(self):
        return self.prenom

    def getAge(self):
        return self.age

    def getProfession(self):
        return self.profession

    def getboostMoral(self):
        return self.boostMoral
    

    def setNom(self,nom):
        self.nom = nom
    
    def setPrenom(self,prenom):
        self.prenom = prenom

    def setAge(self,age):
        self.age = age

    def setProfession(self,profession):
        self.profession = profession

    def setboostMoral(self,boostMoral):
        self.boostMoral = boostMoral

    def __repr__(self):
        return "{}  {}  {}  {}  {}".format(self.nom,self.prenom,self.age,self.profession,self.boostMoral)
