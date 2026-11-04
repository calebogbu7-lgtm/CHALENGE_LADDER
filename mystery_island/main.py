from game import (
    new_game,
    available_item,
    available_locations,
    collect_item,
    move_player,
    make_decision,
    solve_lighthouse_puzzle
)


def display_intro():
    print("=" * 40)
    print("          MYSTERY ISLAND")
    print("         THE LOST LIGHTHOUSE")
    print("=" * 40)

    print("""
A terrible storm has left you stranded
on a mysterious island.

The lighthouse is dark, and the bridge
is locked. Your mission is to explore
the island, find useful objects and
restore the lighthouse.

GAME INSTRUCTIONS
----------------------------------------
1. Collect useful objects.
2. Explore the island.
3. Make important decisions.
4. Discover clues to help solve the puzzle.
5. Manage your energy.
6. Restore the lighthouse to escape.
""")


def display_scene(player):
    item = available_item(player)

    if item is None:
        item_status = "None"
    elif item in player["inventory"]:
        item_status = f"{item} (already collected)"
    else:
        item_status = item

    print("\n" + "-" * 40)
    print(f"Player: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Energy: {player['energy']}")
    print(f"Inventory: {player['inventory'] or 'Empty'}")
    print(f"Available item: {item_status}")
    print(f"Clues: {player['clues'] or 'None'}")
    print("-" * 40)


def display_menu():
    print("\nWhat would you like to do?")
    print("1. Collect available item")
    print("2. Move to another location")
    print("3. Explore location")
    print("4. View inventory")
    print("5. View player status")
    print("6. Quit game")


def play_game():
    display_intro()

    name = input("Enter your name: ").strip()

    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter your name: ").strip()

    player = new_game(name)

    print(f"\nWelcome, {player['name']}!")
    print("You wake up on the Beach.")

    while not player["game_over"]:
        display_scene(player)
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print(collect_item(player))

        elif choice == "2":
            destinations = available_locations(player)

            print("\nAvailable destinations:")

            for index, destination in enumerate(destinations, start=1):
                print(f"{index}. {destination}")

            destination_choice = input("Choose a destination: ").strip()

            selected_destination = None

            if destination_choice.isdigit():
                index = int(destination_choice) - 1

                if 0 <= index < len(destinations):
                    selected_destination = destinations[index]

            else:
                for destination in destinations:
                    if destination_choice.casefold() == destination.casefold():
                        selected_destination = destination
                        break

            if selected_destination is None:
                print(
                    "Invalid destination. "
                    "Please choose one of the listed locations."
                )
            else:
                print(move_player(player, selected_destination))

        elif choice == "3":
            location = player["location"]

            if location == "Lighthouse":
                answer = input(
                    "\nEnter the three symbols in the correct order: "
                )

                print(solve_lighthouse_puzzle(player, answer))
                continue

            exploration_options = {
                "Beach": [
                    "Investigate the area",
                    "Ignore the clue"
                ],
                "Jungle": [
                    "Take the safe path",
                    "Take the longer route"
                ],
                "Cave": [
                    "Study the symbols",
                    "Leave without investigating"
                ]
            }

            if location not in exploration_options:
                print("\nThere are no decisions to make here.")
                continue

            print("\nAvailable decisions:")

            for index, option in enumerate(
                exploration_options[location],
                start=1
            ):
                print(f"{index}. {option}")

            decision_choice = input("\nEnter your decision: ").strip()

            print(make_decision(player, decision_choice))

        elif choice == "4":
            print("\nYOUR INVENTORY")

            if player["inventory"]:
                for item in player["inventory"]:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")

        elif choice == "5":
            print("\nPLAYER STATUS")
            print(f"Name: {player['name']}")
            print(f"Location: {player['location']}")
            print(f"Energy: {player['energy']}")
            print(f"Game over: {player['game_over']}")
            print(f"Victory: {player['won']}")

        elif choice == "6":
            player["game_over"] = True
            print("\nYou have left Mystery Island.")

        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")

    if player["energy"] <= 0 and not player["won"]:
        print("\nYour energy has run out. You have lost the game.")


def main():
    while True:
        play_game()

        replay = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if replay not in ("yes", "y"):
            print("\nThank you for playing Mystery Island!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing Mystery Island!")