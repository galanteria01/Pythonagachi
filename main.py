from classes.game import pet

#Initialising game
print("Welcome to Pythonagachi Simulator Application")
difficulty_level = int(input("Enter the difficulty level: "))
name=input("Enter the name of your pet: ").capitalize()

#Initialising player
player=pet(name,difficulty_level,0,0,0,0)

choice=["eat","play","sleep","take a bath","forage for food"]


running=True
i=1
while running:
   print("Round",str(i))
   print("\n")
   player.details()
   running=False