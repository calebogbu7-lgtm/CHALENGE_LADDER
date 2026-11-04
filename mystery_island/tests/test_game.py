import unittest

from game import (
    new_game,
    available_item,
    available_locations,
    collect_item,
    move_player,
    make_decision,
    solve_lighthouse_puzzle
)


class TestNewGame(unittest.TestCase):

    def test_new_game_has_correct_initial_state(self):
        player = new_game("Caleb")

        self.assertEqual(player["name"], "Caleb")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertEqual(player["decisions_made"], [])
        self.assertEqual(player["clues"], [])
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])


class TestItemCollection(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Caleb")

    def test_player_can_collect_rope_at_beach(self):
        result = collect_item(self.player)

        self.assertIn("Rope", self.player["inventory"])
        self.assertIn("successfully", result)

    def test_player_cannot_collect_same_item_twice(self):
        collect_item(self.player)
        result = collect_item(self.player)

        self.assertEqual(self.player["inventory"], ["Rope"])
        self.assertIn("already collected", result)

    def test_player_cannot_collect_item_at_location_without_one(self):
        self.player["location"] = "Cave"

        result = collect_item(self.player)

        self.assertEqual(self.player["inventory"], [])
        self.assertIn("no item available", result)

    def test_player_can_collect_lantern_in_jungle(self):
        self.player["location"] = "Jungle"

        collect_item(self.player)

        self.assertIn("Lantern", self.player["inventory"])


class TestPlayerMovement(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Caleb")

    def test_player_can_move_to_jungle(self):
        result = move_player(self.player, "Jungle")

        self.assertEqual(self.player["location"], "Jungle")
        self.assertEqual(self.player["energy"], 4)
        self.assertIn("Jungle", result)

    def test_invalid_movement_does_not_cost_energy(self):
        result = move_player(self.player, "Lighthouse")

        self.assertEqual(self.player["location"], "Beach")
        self.assertEqual(self.player["energy"], 5)
        self.assertIn("cannot move", result)

    def test_player_cannot_cross_bridge_without_rope(self):
        self.player["location"] = "Cave"

        result = move_player(self.player, "Old Bridge")

        self.assertEqual(self.player["location"], "Cave")
        self.assertEqual(self.player["energy"], 5)
        self.assertIn("Rope", result)

    def test_player_cannot_enter_lighthouse_without_lantern(self):
        self.player["location"] = "Old Bridge"

        result = move_player(self.player, "Lighthouse")

        self.assertEqual(self.player["location"], "Old Bridge")
        self.assertEqual(self.player["energy"], 5)
        self.assertIn("Lantern", result)

    def test_energy_reaching_zero_ends_game(self):
        self.player["energy"] = 1

        move_player(self.player, "Jungle")

        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(self.player["game_over"])


class TestPlayerDecisions(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Caleb")

    def test_beach_decision_records_clue(self):
        make_decision(self.player, "1")

        self.assertIn(
            "The lighthouse needs three symbols.",
            self.player["clues"]
        )
        self.assertIn("Beach", self.player["decisions_made"])

    def test_player_cannot_repeat_decision(self):
        make_decision(self.player, "1")
        result = make_decision(self.player, "1")

        self.assertIn("already made", result)

    def test_longer_jungle_route_costs_energy(self):
        self.player["location"] = "Jungle"

        make_decision(self.player, "2")

        self.assertEqual(self.player["energy"], 4)


class TestLighthousePuzzle(unittest.TestCase):

    def setUp(self):
        self.player = new_game("Caleb")
        self.player["location"] = "Lighthouse"
        self.player["inventory"].append("Lantern")

    def test_correct_answer_wins_game(self):
        result = solve_lighthouse_puzzle(
            self.player,
            "SUN-MOON-STAR"
        )

        self.assertTrue(self.player["won"])
        self.assertTrue(self.player["game_over"])
        self.assertIn("won", result)

    def test_wrong_answer_costs_energy(self):
        solve_lighthouse_puzzle(
            self.player,
            "SUN-STAR-MOON"
        )

        self.assertEqual(self.player["energy"], 4)
        self.assertFalse(self.player["won"])

    def test_wrong_answer_with_last_energy_ends_game(self):
        self.player["energy"] = 1

        solve_lighthouse_puzzle(self.player, "WRONG")

        self.assertEqual(self.player["energy"], 0)
        self.assertTrue(self.player["game_over"])
        self.assertFalse(self.player["won"])


class TestCompleteWinningJourney(unittest.TestCase):

    def test_player_can_complete_the_game(self):
        player = new_game("Caleb")

        collect_item(player)
        move_player(player, "Jungle")

        collect_item(player)
        move_player(player, "Cave")

        move_player(player, "Old Bridge")
        move_player(player, "Lighthouse")

        result = solve_lighthouse_puzzle(
            player,
            "SUN-MOON-STAR"
        )

        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])
        self.assertEqual(player["energy"], 1)
        self.assertIn("won", result)


if __name__ == "__main__":
    unittest.main()