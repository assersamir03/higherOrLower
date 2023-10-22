import art
import random
from game_data import data

counter = 0
goOn = True
print(art.logo)

while goOn:
    def comparison(fighter1, fighter2):
        if fighter1['follower_count'] > fighter2['follower_count']:
            return True
        else:
            return False


    def gettingThePeople():
        theFirst = random.choice(data)
        data.remove(theFirst)
        theSecond = random.choice(data)
        data.remove(theSecond)
        return theFirst, theSecond


    fighters = gettingThePeople()
    print(f"it is {fighters[0]['name']} with {fighters[0]['follower_count']} follower!! {art.vs} {fighters[1]['name']}")
    theRes = comparison(fighters[0], fighters[1])
    playerChoice = input('which do u think has more followers? A/B: ').capitalize()
    if playerChoice == 'A':
        if theRes:
            counter += 1
        else:
            goOn = False
            print(f"u lost!\nur score is {counter}!")
    elif playerChoice == 'B':
        if theRes == False:
            counter += 1
        else:
            goOn = False
            print(f"u lost!\nur score is {counter}!")
    else:
        print("please enter A or B")
        exit()
