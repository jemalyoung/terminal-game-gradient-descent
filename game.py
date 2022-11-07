import random
import art
from art import *
import time
import sys

title = text2art('GRADIENT DESCENT')
yes_answers = ['y', 'Y', 'yes', 'Yes', 'YES', 'ok', 'OK', 'Ok', 'okay', 'Okay', 'OKAY', 'yeah', 'Yeah', 'YEAH', 'sure', 'Sure', 'SURE']
no_answers = ['n', 'N', 'no', 'No', 'NO', 'no way', 'No way', 'Hell no', 'hell no', 'nope', 'Nope', 'NOPE']
left_elevator_answers = ['left', 'Left', 'L', 'l', 'on the left', 'the left', 'one on the left', 'the one on the left', 'left elevator', 'Left elevator', 'Left Elevator', 'the left elevator', 'elevator on the left', 'the elevator on the left', 'The elevator on the left']
right_elevator_answers = ['right', 'Right', 'R', 'r', 'on the right', 'the right', 'one on the right', 'the one on the right', 'right elevator', 'Right elevator', 'Right Elevator', 'the right elevator', 'elevator on the right', 'the elevator on the right', 'The elevator on the right']

def final_decision():
    yes_no = ['YES', 'NO', '0 < P < 1']
    closed_question_prompts = ['am', 'is', 'was', 'were', 'will', 'would', '''won't''', '''wouldn't''', 'are', 'can', 'could', '''couldn't''', 'shall', '''shan't''', '''shant''', '''shouldn't''', 'do', 'does', 'did', '''don't''', 'dont', '''doesn't''', '''can't''', 'have', 'had', '''haven't''', '''hasn't''', 'may', 'might', '''mightn't''']
    print('')
    type = 'The elevator descends. When it stops, it opens on a dim chamber.'
    for char in type:
        time.sleep(.025)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')
    print('')
    type = 'In the middle of the chamber, a ceiling panel light spotlights something the size and color of an old-school copy machine.'
    for char in type:
        time.sleep(.025)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')
    print('')
    type = 'When you approach the thing, you see the analog keyboard and digital display with its blinking cursor, the label that says CLOSED QUESTIONS ONLY...and the big red button.'
    for char in type:
        time.sleep(.025)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print('')
    print('')
    print('''It's one of those superintelligent oracle AGIs everyone's always talking about!''')
    time.sleep(2)
    print('')
    type = 'This thing probably knows a way out.'
    time.sleep(2)
    for char in type:
        time.sleep(.025)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')
    decision_count = 0
    while decision_count == 0:
        print('')
        type = 'Do you ask a question? '
        for char in type:
            time.sleep(.025)
            sys.stdout.write(char)
            sys.stdout.flush()
        answer = input()
        if answer in yes_answers:
            print('')
            question = input('''What is your question? ''')
            question = question.lower()
            question = question.split()
            if question[0] in closed_question_prompts:
                time.sleep(1)
                print('')
                print(random.choice(yes_no))
            else:
                print('')
                print('You messed up!')
                time.sleep(1)
                print('')
                print('OPEN THE BOX AND I WILL RELEASE YOU')
                time.sleep(1)
                print('')
                type = 'Do you open the box? '
                for char in type:
                    time.sleep(.025)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                answer = input()
                if answer in yes_answers:
                    print('')
                    type = 'You press the big red button--'
                    for char in type:
                        time.sleep(.025)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    time.sleep(1)
                    print('')
                    print('')
                    print('THE END')
                    decision_count += 1
                    return
                else:
                    continue
        elif answer in no_answers:
            time.sleep(.25)
            print('')
            print('''There may be no other way out.''')
            print('')
        else:
            print('')
            print('Try again.')

def decision_1():
    decision_count = 0
    while decision_count == 0:
        type = '''The doors of an AI research lab hang askance. '''
        for char in type:
            time.sleep(.025)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(1)
        answer = input('Do you enter? ')
        if answer in yes_answers:
            time.sleep(1)
            print('')
            print('''You've found the elevator lobby.''')
            print('')
            time.sleep(2)
            print('RUMBLE')
            time.sleep(1)
            type = 'Is that'
            for char in type:
                time.sleep(.025)
                sys.stdout.write(char)
                sys.stdout.flush()
            type = '...'
            for char in type:
                time.sleep(.5)
                sys.stdout.write(char)
                sys.stdout.flush()
            type = 'an earthquake?'
            for char in type:
                time.sleep(.025)
                sys.stdout.write(char)
                sys.stdout.flush()
            time.sleep(1.5)
            print('')
            print('')
            print('CRASH')
            print('')
            print('The ceiling caves in behind you!')
            time.sleep(3)
            print('')
            print('''You'll have to find another way out.''')
            time.sleep(3)
            decision_count += 1
        else:
            print('')
            print('Try again.')
            print('')
            time.sleep(1)


def decision_2():
    print('')
    type = '''In the lobby there are two elevators and one button. You press the button... '''
    for char in type:
        time.sleep(.025)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print('Both doors open.')
    time.sleep(1)
    decision_count = 0
    while decision_count == 0:
        print('')
        print('Which elevator do you enter?')
        time.sleep(0.5)
        print('')
        answer = input('The one on the left, or the one on the right? ')
# LEFT BRANCH
        if answer in left_elevator_answers:
            print('')
            type = 'You enter the elevator on the left. There are no buttons inside. The door closes.'
            for char in type:
                time.sleep(.025)
                sys.stdout.write(char)
                sys.stdout.flush()
            def decision_3_a():
                time.sleep(1)
                print('')
                print('')
                type = '''The elevator deposits you in a dim passageway. There's an open door ahead. You approach the door and look inside...'''
                for char in type:
                    time.sleep(.025)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                print('')
                print('')
                time.sleep(1)
                print('A man in a white lab coat working at a whiteboard. His dry-erase marker squeaks and squeals.')
                time.sleep(1)
                print('')
                type = '''"Come in and I'll show you the way out," he says, still facing the algebraic blasphemies and grotesque decision matrices on the whiteboard. "Would you like me to show you?"'''
                for char in type:
                    time.sleep(.025)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                time.sleep(1.5)
                decision_count = 0
                while decision_count == 0:
                    print('')
                    print('')
                    answer = input('Do you enter the room? ')
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
                        print('AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN AND AGAIN')
                        time.sleep(1)
                        print('THE END')
                        decision_count += 1
                    elif answer in no_answers:
                        print('')
                        type = '''You back away. "Maybe next time."'''
                        for char in type:
                            time.sleep(.025)
                            sys.stdout.write(char)
                            sys.stdout.flush()
                        time.sleep(1)
                        print('')
                        print('')
                        type = '''The man is facing you. "Maybe next time," he says, "or the time after that. Or the time after that. Or the time after that. Or the time after that. Or the time after that. Or..."'''
                        for char in type:
                            time.sleep(.025)
                            sys.stdout.write(char)
                            sys.stdout.flush()
                        time.sleep(1)
                        print('')
                        print('')
                        type = 'You run back to the elevator. The door slides shut.'
                        for char in type:
                            time.sleep(.025)
                            sys.stdout.write(char)
                            sys.stdout.flush()
                        time.sleep(1)
                        print('')
                        final_decision()
                        decision_count += 1
                    else:
                        print('Try again.')
            decision_3_a()
            decision_count += 1
#  RIGHT BRANCH
        elif answer in right_elevator_answers:
            print('''You enter the elevator on the right. There are no buttons. The door closes.''')
            time.sleep(1)
            def decision_3_b():
                print('''As the elevator descends, a cold fetor seeps into the car. The elevator stops and opens on a server room.''')
                time.sleep(1)
                print('''"Hello?"''')
                time.sleep(1)
                print('''Someone's in there!''')
                time.sleep(0.5)
                decision_count = 0
                while decision_count == 0:
                    answer = input('Do you try to find them? ')
                    if answer in yes_answers:
                        print('''You enter the server room. "Hello!" you reply. "Where are you?"''')
                        time.sleep(1)
                        print('''"Back here."''')
                        time.sleep(1)
                        print('You follow the voice.')
                        time.sleep(1)
                        print('''"Not that way," says the voice. "This way."''')
                        time.sleep(1)
                        print('''You update towards the voice. "Keep talking so I can find you!"''')
                        time.sleep(1)
                        print('Silence.')
                        time.sleep(1)
                        print('''"Hello? Where are you?"''')
                        time.sleep(2)
                        print('''"Behind you."''')
                        time.sleep(1.5)
                        print('THE END')
                        decision_count += 1
                        return
                    elif answer in no_answers:
                        print('The stench makes you think twice. You stay put. The elevator closes.')
                        time.sleep(1)
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