print("Celebrity Quiz!!!!!!")
print("Which celebrity are you? Answer thes few questions and find out :)")
answer = input("Do you enjoy dancing")

if answer == "no":
    print("next question")
elif answer == "yes":
    print("next question")
answer2 = input("If answered yes ignore. If answered no are you an introvert?")

if answer2 == "yes":
    print("You are Adelle")
elif answer == "no":
    print("You are Will Smith")
answer3 = input("If you answered that you like to dance, are you into hiphop/r&B?")

if answer3 == "yes":
    print("You are Beyonce!")
elif answer3 == "no":
    print("You are Ariana Grande")
answer4 = input("Which celbrity are you?")

if answer4 == "Will Smith":
    print("Lets find out what Will Smith character you are")
elif answer4 == "Adelle":
    print("lets find out what Adelle Song you are")
elif answer4 == "Ariana Grande":
    print("lets find out What ariana grande show you are from")
answer5 = input("If you are Will Smith, do you enjoy comedies orr dramas? If you arent Will smith, continue")

if answer5 == "comedies":
    print("You are the FRESH PRINCE OF BEL AIR")
elif answer5 == "dramas":
    print("You Are Chris Gardner from Pursuit of Happyness")