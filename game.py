import random
import art
from art import *
import time

title = text2art('GRADIENT DESCENT')
yes_answers = ['y', 'Y', 'yes', 'Yes', 'YES', 'ok', 'OK', 'Ok', 'okay', 'Okay', 'OKAY', 'yeah', 'Yeah', 'YEAH', 'sure', 'Sure', 'SURE']
no_answers = ['n', 'N', 'no', 'No', 'NO', 'no way', 'No way', 'Hell no', 'hell no', 'nope', 'Nope', 'NOPE']
left_elevator_answers = ['left', 'Left', 'L', 'l', 'on the left', 'the left', 'one on the left', 'the one on the left', 'left elevator', 'Left elevator', 'Left Elevator', 'the left elevator', 'elevator on the left', 'the elevator on the left', 'The elevator on the left']
right_elevator_answers = ['right', 'Right', 'R', 'r', 'on the right', 'the right', 'one on the right', 'the one on the right', 'right elevator', 'Right elevator', 'Right Elevator', 'the right elevator', 'elevator on the right', 'the elevator on the right', 'The elevator on the right']

def final_decision():
    yes_no = ['YES', 'NO', '0 < P < 1']
    closed_question_prompts = ['am', 'is', 'was', 'were', 'will', 'would', '''won't''', '''wouldn't''', 'are', 'can', 'could', '''couldn't''', 'shall', '''shan't''', '''shant''', '''shouldn't''', 'do', 'does', 'did', '''don't''', 'dont', '''doesn't''', '''can't''', 'have', 'had', '''haven't''', '''hasn't''', 'may', 'might', '''mightn't''']
    print('''The elevator descends. When it stops, it opens on a dim chamber. In the middle of the chamber, something the size and color of an old-school copy machine is spotlighted from above. When you approach the thing, you see the analog keyboard and digital display with its blinking cursor, and the all-caps label that says CLOSED QUESTIONS ONLY.''')
    decision_count = 0
    while decision_count == 0:
        answer = input('Do you ask a question? ')
        if answer in yes_answers:
            question = input('''What is your question? ''')
            question = question.lower()
            question = question.split()
            if question[0] in closed_question_prompts:
                print(random.choice(yes_no))
            else:
                print('You messed up!')
                print('OPEN THE BOX AND I WILL RELEASE YOU')
                answer = input('Do you open the box? ')
                if answer in yes_answers:
                    print('You type HOW DO I OPEN THE BOX?')
                    print('The display says YOU JUST DID.')
                    print('THE END')
                    decision_count += 1
                    return
                else:
                    continue
        elif answer in no_answers:
            print('''There may be no other way out.''')
        else:
            print('Try again.')

def decision_1():
    decision_count = 0
    while decision_count == 0:
        answer = input('''The doors of an AI research lab hang askance. Do you enter? ''')
        if answer in yes_answers:
            print('''You've found the elevator lobby.''')
            time.sleep(1)
            print('Is that...an earthquake?')
            time.sleep(1.5)
            print('The ceiling caves in behind you!')
            time.sleep(1)
            print('''You'll have to find another way out.''')
            decision_count += 1
        else:
            print('Try again.')

time.sleep(1.25)
def decision_2():
    print('''There are two elevators in the lobby. You press the button...''')
    time.sleep(1)
    print('Both doors open.')
    time.sleep(1)
    decision_count = 0
    while decision_count == 0:
        print('Which elevator do you enter?')
        time.sleep(1)
        answer = input('The one on the left, or the one on the right? ')
# LEFT BRANCH
        if answer in left_elevator_answers:
            time.sleep(1)
            print('You enter the elevator on the left. There are no buttons. The door closes.')
            def decision_3_a():
                time.sleep(1)
                print('''The elevator deposits you in a dim passageway. There's an open door ahead. You approach the door and look inside...''')
                time.sleep(1)
                print('A man in a white lab coat working at a whiteboard. His dry-erase marker squeaks and squeals.')
                time.sleep(1)
                print('''"Come in and I'll show you the way out," he says, still facing the algebraic blasphemies and grotesque decision matrices on the whiteboard. "Would you like me to show you?"''')
                time.sleep(1)
                decision_count = 0
                while decision_count == 0:
                    answer = input('Do you enter the room? ')
                    time.sleep(1)
                    if answer in yes_answers:
                        print('''You enter the room. The man is gone.''')
                        time.sleep(1.5)
                        print('''"I've shown you the way out," he says from the hallway behind you, and then he's gone. You run through the door, white coattails flying...''')
                        time.sleep(1)
                        print('''"WTF..."''')
                        time.sleep(1)
                        print('''You're back in the room with the whiteboard.''')
                        time.sleep(1)
                        print('You try to get out again.')
                        time.sleep(1)
                        print('And again.')
                        time.sleep(1)
                        print('And again.')
                        time.sleep(0.5)
                        print('And again.')
                        time.sleep(0.5)
                        print('AND AGAIN.')
                        time.sleep(0.5)
                        print('AND AGAIN.')
                        time.sleep(1)
                        print('THE END')
                        decision_count += 1
                    elif answer in no_answers:
                        print('''You back away. "Maybe next time."''')
                        print('''Now the man is facing you. "Maybe next time," he says, "or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or..."''')
                        print('You run back to the elevator. The door slides shut.')
                        final_decision()
                        decision_count += 1
                    else:
                        print('Try again.')
            decision_3_a()
            decision_count += 1
#  RIGHT BRANCH
        elif answer in right_elevator_answers:
            print('''You enter the elevator on the right. There are no buttons. The door closes.''')
            def decision_3_b():
                print('''As the elevator descends, a cold fetor seeps into the car. The elevator stops and opens on a server room.''')
                print('''"Hello?"''')
                print('''Someone's in there!''')
                decision_count = 0
                while decision_count == 0:
                    answer = input('Do you try to find them? ')
                    if answer in yes_answers:
                        print('''You enter the server room. "Hello!" you reply. "Where are you?"''')
                        print('''"Back here."''')
                        print('You follow the voice.')
                        print('''"Not that way," says the voice. "This way."''')
                        print('''You update towards the voice. "Keep talking so I can find you!"''')
                        print('Silence.')
                        print('''"Hello? Where are you?"''')
                        print('''"Behind you."''')
                        print('THE END')
                        decision_count += 1
                        return
                    elif answer in no_answers:
                        print('The stench makes you think twice. You stay put. The elevator closes.')
                        final_decision()
                        decision_count += 1
                    else:
                        print('Try again.')
            decision_3_b()
            decision_count += 1

def start_game():
    print(title)
    decision_1()
    decision_2()

start_game()