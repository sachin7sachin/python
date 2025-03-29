import random
import art
import game_data

def play():
    dictionary_2 = random.choice(game_data.data)

    score_count = 0
    game_over = False
    while not game_over:
        dictionary_1 = dictionary_2
        dictionary_2 = random.choice(game_data.data)
        if dictionary_1 == dictionary_2:
            dictionary_2 = random.choice(game_data.data)

        name_1 = dictionary_1["name"]
        description_1 = dictionary_1["description"]
        country_1 = dictionary_1["country"]

        name_2 = dictionary_2["name"]
        description_2 = dictionary_2["description"]
        country_2 = dictionary_2["country"]


        print("\n" * 20)
        print(art.logo)

        if score_count != 0:
            print(f"That's correct. Your score: {score_count}")

        print(f"Compare A: {name_1}, {description_1}, {country_1}")
        print(art.vs)
        print(f"Against B: {name_2}, {description_2}, {country_2}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess == "a":
            if dictionary_1["follower_count"] > dictionary_2["follower_count"]:
                score_count += 1
            else:
                game_over = True
                print(f"Sorry, that's wrong. Final score: {score_count}")

        elif guess == "b":
            if dictionary_2["follower_count"] > dictionary_1["follower_count"]:
                score_count += 1
            else:
                game_over = True
                print(f"Sorry, that's wrong. Final score: {score_count}")
print(art.logo)
while input("Type 'y' to play or type 'n' to end: ") == "y":
    play()