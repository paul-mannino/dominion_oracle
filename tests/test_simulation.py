from dominion_oracle.simulation import Simulation
from dominion_oracle.cards import library


def assert_close(expected, actual, tolerance=0.05):
    assert abs(expected - actual) <= tolerance


def test_expected_value_of_starting_deck():
    card_list = library.get_cards(["estate"] * 3 + ["copper"] * 7)
    assert_close(3.5, Simulation(card_list).expected_terminal_value())


def test_expected_value_of_deck_with_draw():
    cards = library.get_cards(["copper"] * 7 + ["estate"] * 3 + ["gold", "smithy", "village"])
    simulation = Simulation(cards)
    assert_close(5.205, simulation.expected_terminal_value())


def test_expected_value_of_deck_with_no_value():
    simulation = Simulation(["duchy", "smithy", "village", "laboratory"])
    assert_close(0, simulation.expected_terminal_value())


def test_expected_value_of_treasure_only_deck():
    cards = ["copper"] * 10 + ["silver"] * 3 + ["gold"] * 2
    expected_result = 5 * ((10 + 3 * 2 + 2 * 3) / 15)
    assert_close(expected_result, Simulation(cards).expected_terminal_value())
