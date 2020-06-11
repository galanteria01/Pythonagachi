import random
class pet():
    def __init__(self,name,level,hunger,boredom,tiredness,dirtiness,choice,food_forage,status):
        self.name=name
        self.level=level
        self.hunger=hunger
        self.boredom=boredom
        self.tiredness=tiredness
        self.dirtiness=dirtiness
        self.choice=choice
        self.food_forage=food_forage
        self.status=status




    def details(self):
        print("Creature Name:",self.name)
        print("Hunger(0-10)",self.hunger)
        print("Boredom(0-10)", self.boredom)
        print("Tiredness(0-10)",self.tiredness)
        print("Dirtiness(0-10)",self.dirtiness)
        print("\n")
        print("Food stored",str(self.food_forage))
        print("Status",self.status)

    def get_choices(self,choice):
        i=1
        for cho in choice:
            print("Enter",str(i),"for",cho)
            i+=1

    def eating(self):
        self.hunger=0
        self.food_forage-=1

    def playing(self):
        self.boredom=0
        k=random.randrange(1,self.level)
        self.tiredness+=k
        self.dirtiness+=k
        self.hunger+=k

    def sleeping(self):
        self.tiredness=0
        k=random.randrange(0,self.level)
        self.dirtiness+=k
        self.boredom+=k

    def bathing(self):
        if self.dirtiness<10:
            self.dirtiness=0
        k=random.randrange(0,self.level)
        self.tiredness+=k

    def collect_food(self):
        self.food_forage+=4
        k=random.randrange(0,self.level)
        self.tiredness+=k
        self.dirtiness+=k
        self.hunger+=k



