import random
from art import logo, vs
from game_data import data
from replit import clear


def get_random_person():
    rand_person = random.choice(data)
    return rand_person


def compare(comp_a, comp_b):
    if comp_a["follower_count"] > comp_b["follower_count"]:
        return 'a'
    return 'b'

def format_data(acc):
  name = acc["name"]
  description = acc["description"]
  country = acc["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def play_game():
    # print logo
    game_over = False
    score = 0
    print(logo)

    while not game_over:
        comp_a = get_random_person()
        comp_b = get_random_person()
        while comp_b == comp_a:
            comp_b = get_random_person()

        print(
            f"Compare A: {format_data(comp_a)}."
        )

        print(vs)

        print(
            f"Against B: {format_data(comp_b)}."
        )

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice == compare(comp_a, comp_b):
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            clear()
            print(logo)
            game_over = True
            print(f"Sorry, that's wrong. Final score: {score}")


play_game()
