import random
class pet():
    def __init__(self,name,level,hunger,boredom,tiredness,dirtiness):
        self.name=name
        self.level=level
        self.hunger=hunger
        self.boredom=boredom
        self.tiredness=tiredness
        self.dirtiness=dirtiness


    def details(self):
        print("Creature Name:",self.name)
        print("Hunger(0-10)",self.hunger)
        print("Boredom(0-10)", self.boredom)
        print("Tiredness(0-10)",self.tiredness)
        print("Dirtiness(0-10)",self.dirtiness)





