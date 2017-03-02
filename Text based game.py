print("Who am I? How did I get here? (You rise up, having not remembered anything, not even your identity)")
print("Ughhh! I suppose I should walk around but should I go forward or backwards?")
choice=eval(input("Press 1 for forward and 2 for backwards"))
if choice==1:
    print("Forward it is!")
    print("While pacing forward across the darkly lit area you spot a building named 'Oliver Hall'.")
    print("Should I go look inside? It seems that only the turbo nerds reside there...")
    oliver=eval(input("Type 1 to go inside and 2 to turn and run: "))
    if oliver==1:
        print("Let's go! you yell as you try to open the door.")
        print("It's locked")
        print("Damn, I shoudl have goten 24 access from Nona!....Wait, who's Nona?")
        print("Are my memories coming back?!")
        print("As you pase around for the next 3 minutes, you hear footsteps")
        print("'Howdy!' the voice says.")
        criss=eval(input("Type 1 to challenge him to fight and 2 to run away: "))
        if criss==1:
            print("Yo man, get that beautiful fro outta here! Unless you looking to fight, scram!")
            print("'Oh, I'm always looking to fight' he says while pulling out a controller out of his usual blue sweatshirt")
            print("'Oh I see,' you say 'You wanna settle it in Smash eh?")
            print("'Yep,' he says 'need to work on my Dededee game. Nintendo needs to patch him!")
            print("Suddenly the realization you know what Smash and that this man name is Criss floods your mind")
            print("Ughhh, should you ask him who you are or play Smash with him?")
            smash=eval(input("Type 1 to ask him who you are and 2 to SETTLE IT IN SMASH: "))
            if smash==1:
                print()
            elif smash==2:
                print()
        elif criss==2:
            print()
    elif oliver==2:
        print("Fuck this, I can;t handle this! There's probably nothing but basement dwellers and stench coming from there!")
        print("I guess I'll turn around")
elif choice==2:
    print("Backwards it is!")
