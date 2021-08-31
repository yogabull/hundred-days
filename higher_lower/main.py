# Higher / Lower game from 100 days of Code. Class by Angela Yu.

import art
import game_data
from random import randint
from time import sleep


def main():
    print_header()
    game_loop()


def print_header():  # print header and set score
    print(art.logo + '\n')


def display_person(person):
    padding = '         '
    print(padding + person['name'])
    print(padding + str(person['follower_count']))
    print(padding + person['description'])
    print(padding + person['country'])


def get_person():
    data = game_data.data
    num = randint(0, len(data) - 1)
    person = data[num]
    return person


def game_loop():
    winning = True
    score = 0
    person_A = get_person()

    while winning == True:
        print('\n\n--------------------------------')
        print('            COMPARE\n')
        display_person(person_A)
        sleep(.2)
        print(art.vs + '\n')
        sleep(.2)
        person_B = get_person()
        display_person(person_B)
        sleep(.2)

        guess = str(input('\nWho has more followers? 1 or 2  '))

        if person_A['follower_count'] > person_B['follower_count']:
            # outputs who has more followers.
            answer = '1'
        else:
            answer = '2'

        sleep(1)
        if guess != answer:
            print('INCORRECT')
            winning = False
        else:
            print('\n\nCORRECT')
            score += 1
            print(f"Your score is {score} correct.\n")
            person_A = person_B
        sleep(1)

    print('\nSorry you lose.')
    print(f"Your score was {score} correct\n")


if __name__ == "__main__":
    main()
