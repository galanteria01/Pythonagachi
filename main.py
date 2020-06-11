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
   if player.status=="awake":
      player.get_choices(choices)
      player_choice=int(input("Enter the choice of player: "))
      if player_choice==1:
         player.eating()
      elif player_choice==2:
         player.playing()
      elif player_choice==3:
         player.sleeping()
      elif player_choice==4:
         player.bathing()
      elif player_choice==5:
         player.collect_food()

      print("Your steps have done")
      if player.tiredness > 10:
         player.status = "sleep"
      elif player.hunger >= 10:
         print("Sorry your player has died")
      elif player.boredom >= 10:
         print("Sorry your pet has gone away being bored of you")
      elif player.dirtiness >= 10:
         print("Your player is too shabby")


   elif player.status=="sleep":
      optional=input("Press enter to wake up the pet: ")
      if optional=="":
         print("Yipee your pet has woke up")
         continue
