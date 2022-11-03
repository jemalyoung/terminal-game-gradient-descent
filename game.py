import random
import art
from art import *

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
            print('Is that...an earthquake?')
            print('The ceiling caves in behind you!')
            print('''You'll have to find another way out.''')
            decision_count += 1
        else:
            print('Try again.')


def decision_2():
    print('''There are two elevators in the lobby. You press the button...''')
    print('Both doors open.')
    decision_count = 0
    while decision_count == 0:
        answer = input('Which elevator do you enter? The one on the left, or the one on the right? ')
# LEFT BRANCH
        if answer in left_elevator_answers:
            print('You enter the elevator on the left. There are no buttons. The door closes.')
            def decision_3_a():
                print('''The elevator deposits you in a dim passageway. There's an open door ahead. You approach the door and look inside...''')
                print('A man with his back to you in a white lab coat, busy at a whiteboard.')
                print('''"You're just in time to test my novel decision theory," he says without turning, and your gorge rises at the sight of the algebraic blasphemies and grotesque decision matrices on the whiteboard. "Won't you come in?"''')
                decision_count = 0
                while decision_count == 0:
                    answer = input('Do you enter the room? ')
                    if answer in yes_answers:
                        print('''You enter the room. "I propose Bottomless Decision Theory," the man says as he jumps on you.''')
                        print('THE END')
                        decision_count += 1
                    elif answer in no_answers:
                        print('''You back away. "Maybe next time."''')
                        print('''Now the man is facing you. "Maybe next time," he says, "or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or..."''')
                        print('You run.')
                        print('So does the man in the white coat.')
                        print('''"Or the time after that. Or the time after that. Or the time after that. Or the time..."''')
                        print('You make it to the elevator. The door slides shut.')
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