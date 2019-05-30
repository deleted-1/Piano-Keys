from datetime import datetime

def game():
    past_time = datetime.now()
    present_time = datetime.now()
    keepGoing = True
    while keepGoing:
        if (present_time-past_time).seconds === 4:
            keepGoing = False
            print("Four seconds have passed!")

game()