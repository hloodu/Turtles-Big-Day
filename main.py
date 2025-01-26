###################
# Harman Loodu
# Choose Your Own Adventure - Camping Trip
# March 7 2022
# Go camping; choose where to go, what to take and what to do when there.
###################

# create variables
# variables made within 'if' statements only apply in those statements; so, create them beforehand just in case
# also, some variables might not apply at certain points, depending on how the person played the game. giving them an unrelated value prevents an error from popping up
endGame = "false"
wrong = "false"
campsiteChoice = "x"
transport = "x"
campsite = "x"
packing = "x"
packed = "x" 

# start game
print("Time to go camping!")
print("")

# select campsite
print("There are two campsites. Which are you going to?")

print("(a) - Green Meadows Campsite")

print("(b) - Phantom Hills Campsite")
print("")

campsiteChoice = input("Enter selection: ")
print("") 

# set campsite variables
if campsiteChoice == "a":
  campsite = "Green Meadows Campsite"

elif campsiteChoice == "b":
  campsite = "Phantom Hills Campsite"

else:
  wrong = "true"


# choose what to pack, unless entered something not an option
if wrong == "true":
  print("Try again and enter one of the options.")

else:
  print("What are you packing?")

  print("(a) - A tent, two changes of clothes, and a flashlight")

  print("(b) - Some food, water, and a blanket")

  print("(c) - An air mattress, a tarp, and some trail mix")

  print("(d) - A hammer, a sleeping bag, and a first aid kit")
  print("")

  packing = input("Enter selection: ")
  print("")

# set packed variable
  if packing == "a":
    packed = "tent, clothes, and flashlight"

  elif packing == "b":
    packed = "food, water, and blanket"

  elif packing == "c":
    packed = "air mattress, tarp, and trail mix"

  elif packing == "d":
    packed = "hammer, sleeping bag, and first aid kit"

  else:
    wrong = "true"

  # choose how to get there, unless entered something not an option

  if wrong == "true":
    print("Try again and enter one of the options")

  else:
    print("Alright! Time to go to the", campsite + ".")

    print("How do you get there?")

    print("(a) - Boat")

    print("(b) - City Bus")

    print("(c) - Car")

    print("(d) - Helicopter")
    print("")

    transport = input("Enter selection: ")
    print("")

    # begin adventure, unless entered something not an option
    if wrong == "true":
      print("Try again and enter one of the options.")

    # taking a boat
    elif transport == "a":
      print("You pack up your", packed, "and get in the boat to go to the", campsite + ".")

      # going to phantom hills? game over
      if campsiteChoice == "b":
        print("")
        print("On your way, a storm begins to brew.")
        print("The waves get stronger.")
        print("The wind continues to blow.")
        print("A strong gust and a huge wave push your boat over.")
        print("Your boat capsizes, and your", packed, "are ruined.")
        print("Coast guard quickly comes and rescues you, but it's too late.")
        print("")

        # game over;  variable will stop program from continuing
        endGame = "true"
    
      # otherwise, continue with game.

    # taking a bus
    elif transport == "b":
      print("You gather your", packed, "and catch the next bus to the", campsite + ".")

    # taking a car
    elif transport == "c":
      print("You pack your", packed, "into the car, and start on your way to the", campsite + ".")

    # taking a helicopter
    elif transport == "d":
      print("You book a helicopter flight to the", campsite, "with your", packed, "in hand.")
      print("It's windy.")
      print("...REALLY windy.")
      print("After around ten minutes of flying, your pilot decides to turn around and head back.")
      print("")
  
      endGame = "true"

    else:
      wrong = "true"

    # continue game, but if it has ended, then print a final thing
    if wrong == "true":
      print("Try again and enter one of the options.")
      
    elif endGame == "true":
      print("Your camping trip is over before it even started.")
  
    else: 
      print("")

      # game is different based on which campsite was picked
      if campsiteChoice == "a":
        print("You arrive at the Green Meadows Campsite!")

        print("")

        print("What do you want to do next?")

        print("(a) - Set up camp")

        print("(b) - Eat something")

        print("(c) - Explore a bit")

        print("(d) - Go home")
        print("")

        activity = input("Enter selection: ")
        print("")

        # choose to set up camp
        if activity == "a":
          # set up camp with a tent, clothes and a flashlight
          if packing == "a":
            print("You pitch your tent, and grab your flashlight.")

          # set up with food, water, and a blanket
          elif packing == "b":
            print("You only have a blanket, and you'd prefer to keep that clean for later instead of putting it on the ground.")

          # set up with an air mattress, tarp and trail mix
          elif packing == "c":
            print("You lay out your tarp and go to blow up your air mattress, but realize that you forgot the pump.")
            print("")
            
            print("What do you do?")
            
            print("(a) - Blow it up yourself")

            print("(b) - Look for someone who has a pump")
            print("")

            pump = input("Enter selection: ")
            print("")

            # blow up on own
            if pump == "a":
              print("You start blowing.")
              print("It's taking some time, and you're getting lightheaded.")
              print("You eventually stop - it's taking too long.")
              print("You decide to forget it, and just go home.")
              print("")
              print("Your camping trip is over.")
              endGame = "true"

              # look for help
            elif pump == "b":
              print("You wander around for a bit. You find a group of cabins, but no one has a pump.")
              print("The people offer to let you stay with them, but at this point, you'd rather go home.")
              print("")
              print("Your camping trip is over.")
              endGame = "true"
              
            else:
              wrong = "true"

          # set up with a hammer, sleeping bag and FA kit
          elif packing == "d":
            print("You lay out your sleeping bag. You realize you didn't bring a pillow, but you think you'll manage.")

        # eat something    
        elif activity == "b":
          # brought a tent? can't eat
          if packing == "a":
            print("You didn't bring any food... oh well.")

          # brought food? eat it  
          elif packing == "b":
            print("You open your bag, and pull out your food. It's kind of smushed from the trip here, but it's still good to eat.")

          # brought air mattress? eat trail mix
          elif packing == "c":
            print("You pull out your trail mix. Delicous!")

          # brought FA kit? find berries
          elif packing == "d":
            print("You didn't bring any food, but you find a bush with edible berries.")

        # explore
        elif activity == "c":
          print("You set down your", packed, "and wander around a bit.")
          print("There's a central area with cabins, but not much else.")
          print("You return to your belongings.")

        # leave
        elif activity == "d":
          print("You grab your", packed, "and get ready to leave.")
          # leave according to mode of transport
          if transport == "a":
            print("You wait for the boat to come back.")
            print("When it does, you get in and head home.")

          elif transport == "b":
            print("You catch the next bus home.")

          elif transport == "c":
            print("You get in your car and head home.")

          # no helicopter; trip has already ended for that option

          print("")
          print("Your camping trip is over.")
          endGame = "true"

        else:
          wrong = "true"
        
        # continue, unless game is over
        if wrong == "true":
          print("Try again and enter one of the options.")
          
        elif endGame == "true":
          print("")
          
        else:
          print("")
          print("The sun is starting to set. Now what?")

          print("(a) - Go to sleep")
          print("(b) - Go home")
          print("")

          activity2 = input("Enter selection: ")
          print("")

          # go to sleep
          if activity2 == "a":
            # brought a tent? sleep through the night, game over
            if packing == "a":
              print("You get in your tent and go to sleep.")
              print("")
              print("You wake up the next morning.")
              print("You've had a great camping trip, and it's time to go home.")
              print("")
              print("Your camping trip is over.")
              endGame == "true"

            # brought a blanket? too cold, go home
            elif packing == "b":
              print("You get under your blanket.")
              print("The grass is cold, and you can't sleep.")
              print("You decide to just go home.")
              print("")
              print("Your camping trip is over.")
              endGame == "true"

            # brought an air mattress? it has a hole, go home
            elif packing == "c":
              print("You lay out your tarp, but when you go to set up your air mattress, you realize there's a hole in it.")
              print("It's too late to deal with this. You decide to go home and sleep on a REAL mattress.")
              print("")
              print("Your camping trip is over.")
              endGame == "true"

            # brought a sleeping bag? there's a strange sound
            elif packing == "d":
              print("You get in your sleeping bag and are about to fall asleep when you hear a strange sound.")
              print("")
              print("What do you do?")
              
              print("(a) - Investigate")
              print("(b) - Ignore it and go to sleep")
              print("")
              
              sound = input("Enter selection: ")
              print("")

              # investigate sound
              if sound == "a":
                print("You grab your hammer and creep towards the sound.")
                print("It gets louder, but the wind stops blowing and the sound suddenly pauses.")
                print("You swing your hammer, but it doesn't hit anything.")
                print("Upon further investigation, it was just a bush blowing in the wind.")

                print("")
                print("You go back to bed and sleep through the rest of the night.")
                print("You wake up the next morning. You've had a successful camping trip and decide to go home.")
                print("")
                print("Your camping trip is over.")
                endGame = "true"

              # go back to sleep
              elif sound == "b":
                print("You turn over and go to sleep.")
                print("")
                print("The next morning, you look around, and realize the sound was probably just those bushes over there.")
                print("You've have a good camping trip, and decide to go home.")
                print("")
                print("Your camping trip is over.")
                endGame = "true"

              else:
                wrong = "true"
        
          # go home
          elif activity2 == "b":
            print("You decide your camping trip has been a good one.")
            
            # leave according to mode of transport
            # by boat
            if transport == "a":
              print("You wait for the boat to come back.")
              print("When it does, you get in and head home.")

            # by bus
            elif transport == "b":
              print("You catch the next bus home.")

            # by car
            elif transport == "c":
              print("You get in your car and head home.")
              
            print("")
            print("Your camping trip is over.")
            endGame = "true"
            
          else:
            wrong = "true"

          if wrong == "true":
            print("Try again and enter one of the options.")

          elif endGame == "true":
            print("")

      # if went to phantom hills, game over
      elif campsiteChoice == "b":
        print("You arrive at the Phantom Hills Campsite.")

        print("")
        print("As you walk to your camping spot, the wind blows.")
        print("Your", packed, "fly from your hands.")
        print("You won't be able to camp without them, but you decide to continue on, just to see what's ahead.")
        print("")
        print("You reach your camping spot.")
        print("The dirt is now mud, and you hear thuds from the woods to your right.")
        print("...Nope!")
        print("You turn around and head home.")

        print("")
        print("Your camping trip is over.")
        endGame = "true"

      else:
        wrong = "true"

      if endGame == "true":
        print("")
      
      elif wrong == "true":
        print("")
