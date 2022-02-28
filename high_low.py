from art import logo, vs
from game_data import data
import random


def game():
    score = 0
    not_lost_yet = True
    A = random.choice(data)
    B = random.choice(data)

    while A == B:
        B = random.choice((data))

    def who_wins(guess):
        if A['follower_count'] > B['follower_count']:
            return "A"
        elif A['follower_count'] < B['follower_count']:
            return "B"
        else:
            return guess

    while not_lost_yet:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Chose A: {A['name']}, {A['description']} from {A['country']}")
        print(vs)
        print(f"Against B: {B['name']}, {B['description']} from {B['country']}") 
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        winner = who_wins(guess)
        if guess == winner:
            score += 1
            A = B
            B = random.choice(data)
        else:
            print(f'You lost, you scored {score}.')
            not_lost_yet = False
    again = input("Type 'y' to play again or 'n' to quit: ").lower()
    if again == 'y':
        game()

game()
