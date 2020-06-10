from classes.game import pet

#Initialising game
print("Welcome to Pythonagachi Simulator Application")
difficulty_level = int(input("Enter the difficulty level: "))
name=input("Enter the name of your pet: ").capitalize()
choices=["eat","play","sleep","take a bath","forage for food"]

#Initialising player
player=pet(name,difficulty_level,0,0,0,0,choices,2,"awake")



running=True
i=1
while running:
   print("Round",str(i))
   print("\n")
   player.details()
   player.get_choices(choices)
   player_choice=int(input("Enter the choice of player: "))
   if player_choice==1:
      player.eating()
   elif player_choice==2:
      player.playing()
   elif player_choice==3:



   running=False