import random
inventory = []
# game loop


def main():
    print("Welcome to the Enchanted Quest Game!")
    print("Get ready to be a hero on a quest to save a magical kingdom.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Talk to a villager")
        print("2. Explore the forest")
        print("3. Enter the cave")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            talk_to_villager()
        elif choice == "2":
            explore_forest()
        elif choice == "3":
            enter_cave()
        elif choice == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

# interaction with a friendly villager


def talk_to_villager():
    print("\nYou engage in conversation with a friendly villager.")
    print("He reveals a secret about a hidden treasure in the forest.")
    input("Press Enter to continue...")

# exploring the mysterious forest


def explore_forest():
    global inventory

    print("\nYou venture into the dense forest and come across a mysterious clearing.")
    print("A riddle is inscribed on a stone: 'I'm tall when I'm young and short when I'm old. What am I?'")
    answer = input("Enter your answer: ")

    if answer.lower() == "candle":
        print("Congratulations! You've solved the riddle and discovered a treasure!")
        print("You now possess a key that might prove valuable later.")
        inventory.append("key")
        input("Press Enter to continue...")
        explore_forest_with_key()
    else:
        print("Oops! That's incorrect. You continue your exploration.")

# exploring the forest with the key


def explore_forest_with_key():
    global inventory

    print("\nUsing the newfound key, you uncover a hidden path leading deeper into the forest.")
    print("Here, you stumble upon a locked chest.")

    if "key" in inventory:
        choice = input("Do you want to 'open' the chest or 'leave' it? ")

        if choice.lower() == "open":
            print("You unlock the chest with the key and find valuable treasures inside!")
            inventory.append("treasure")
            input("Press Enter to continue...")
        elif choice.lower() == "leave":
            print("You decide to leave the chest untouched and continue your journey.")
            input("Press Enter to continue...")
    else:
        print("You lack the key to open the chest.")
        input("Press Enter to continue...")

# entering a dark and ominous cave


def enter_cave():
    print("\nYou cautiously step into the darkness of a cave.")
    print("Inside, a fearsome dragon guards a pile of glittering gold.")
    choice = input(
        "Do you want to 'sneak' past the dragon, 'fight' it, or 'leave'? ")

    if choice.lower() == "sneak":
        print("You manage to sneak past the dragon, securing a portion of the gold!")
        inventory.append("gold")
    elif choice.lower() == "fight":
        if dragon_fight():
            print("Congratulations! You defeat the dragon and claim the gold!")
            inventory.append("gold")
        else:
            print("The dragon's might overpowers you, and you are defeated.")
    else:
        print("Your hesitation is brief as the dragon awakens, forcing a hasty retreat.")

# engaging in a battle of wits against the dragon


def dragon_fight():
    print("\nYou decide to confront the dragon head-on.")
    print("The dragon presents you with a riddle that can weaken it.")
    print("Guess correctly to deal damage to the dragon!")

    for _ in range(1):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 11)
        print("\t\tHint : Think of a two-digit number")
        player_answer = int(input("Enter your guess: "))
        if num1 == player_answer or num2 == player_answer:
            print("Correct! You strike a perfect blow to the dragon!")
        else:
            print("Incorrect! The dragon retaliates!")
            return False

    return True


# start the game
if __name__ == "__main__":
    main()
