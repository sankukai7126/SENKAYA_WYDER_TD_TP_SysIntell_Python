import Character

class Army:
    def __init__(self, chef, valeur_Moral):
        self.chef = chef
        self.valeur_Moral = valeur_Moral

    def get_Chef(self):
        return self.chef

    def get_Moral(self):
        return self.valeur_Moral

    def set_Chef(self, chef):
        self.chef = chef

    def set_Moral(self, moral):
        self.valeur_Moral = moral

    def __repr__(self):
        return "{}  {}".format(self.chef.nom, self.valeur_Moral)

    def get_total_moral(self):
        S = self.valeur_Moral * self.get_Chef().getboostMoral()
        return S