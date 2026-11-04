def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "decisions_made": [],
        "clues": [],
        "game_over": False,
        "won": False
    }


def available_item(player):
    items = {
        "Beach": "Rope",
        "Jungle": "Lantern"
    }

    return items.get(player["location"])


def available_locations(player):
    routes = {
        "Beach": ["Jungle"],
        "Jungle": ["Beach", "Cave"],
        "Cave": ["Jungle", "Old Bridge"],
        "Old Bridge": ["Cave", "Lighthouse"],
        "Lighthouse": ["Old Bridge"]
    }

    return routes[player["location"]]


def collect_item(player):
    if player["game_over"]:
        return "The game has already ended."

    if player["energy"] <= 0:
        return "You have no energy remaining."

    item = available_item(player)

    if item is None:
        return "There is no item available here."

    if item in player["inventory"]:
        return f"You have already collected the {item}."

    player["inventory"].append(item)

    return f"You collected the {item} successfully."


def move_player(player, destination):
    if player["game_over"]:
        return "The game has already ended."

    if player["energy"] <= 0:
        return "You have no energy remaining."

    destination = destination.strip().title()

    if destination not in available_locations(player):
        return "You cannot move to that location."

    if destination == "Old Bridge" and "Rope" not in player["inventory"]:
        return "You need the Rope to cross the Old Bridge."

    if destination == "Lighthouse" and "Lantern" not in player["inventory"]:
        return "You need the Lantern to enter the Lighthouse."

    player["location"] = destination
    player["energy"] -= 1

    if player["energy"] <= 0:
        player["game_over"] = True

    return f"You moved to {destination}."


def make_decision(player, choice):
    if player["game_over"]:
        return "The game has already ended."

    if player["energy"] <= 0:
        return "You have no energy remaining."

    decisions = {
        "Beach": {
            "1": ("You discover a clue about the lighthouse.", "Beach clue discovered."),
            "2": ("You ignore the clue.", "No clue discovered.")
        },
        "Jungle": {
            "1": ("You discover a safe path through the jungle.", "Safe path discovered."),
            "2": ("You take the longer route.", "You lose valuable time.")
        },
        "Cave": {
            "1": ("You discover the lighthouse symbol sequence.", "Puzzle clue discovered."),
            "2": ("You leave the cave without investigating.", "No puzzle clue discovered.")
        }
    }

    location = player["location"]

    if location not in decisions:
        return "There are no decisions to make here."

    if location in player["decisions_made"]:
        return "You have already made a decision here."

    choice = choice.strip()

    if choice not in decisions[location]:
        return "Invalid decision."

    player["decisions_made"].append(location)

    if location == "Beach" and choice == "1":
        player["clues"].append("The lighthouse needs three symbols.")

    elif location == "Cave" and choice == "1":
        player["clues"].append("The correct sequence is SUN-MOON-STAR.")

    if location == "Jungle" and choice == "2":
        player["energy"] -= 1

        if player["energy"] <= 0:
            player["game_over"] = True

    message, consequence = decisions[location][choice]

    return f"{message}\n{consequence}"


def solve_lighthouse_puzzle(player, answer):
    if player["game_over"]:
        return "The game has already ended."

    if player["energy"] <= 0:
        return "You have no energy remaining."

    if player["location"] != "Lighthouse":
        return "You must reach the Lighthouse first."

    if "Lantern" not in player["inventory"]:
        return "You need the Lantern to light the Lighthouse."

    answer = answer.strip().upper().replace("-", "").replace(" ", "")

    if answer == "SUNMOONSTAR":
        player["won"] = True
        player["game_over"] = True

        return "Correct! You have restored the Lighthouse and won the game."

    player["energy"] -= 1

    if player["energy"] <= 0:
        player["game_over"] = True
        return "Incorrect answer. You have run out of energy."

    return f"Incorrect answer. You have {player['energy']} energy remaining."