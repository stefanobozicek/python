wlc = "welcome to the mood checker!"

print(wlc)

mood = input("What is your mood today Sir? (choose between good, sad, excited and relaxed): ")

if  mood == "good":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Take a beer, come back and I will ask you again.")
elif mood == "excited":
    print("If so, let's do some action!")
elif mood == "relaxed":
    print("No need to take a breath")
else:
    print("I don't recognize this mood!")


