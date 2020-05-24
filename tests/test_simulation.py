from dominion_oracle.simulation import Simulation
from dominion_oracle.cards import create_card


def test_expected_value_of_starting_deck():
    card_list = [create_card(name) for name in ["estate"] * 3 + ["copper"] * 7]
    simulation = Simulation(card_list)
    assert abs(simulation.expected_terminal_value() - 3.5) < 0.05


def test_expected_value_of_deck_with_draw():
    cards = ["copper"] * 7 + ["estate"] * 3 + ["gold", "smithy", "village"]
    simulation = Simulation([create_card(name) for name in cards])
    assert abs(simulation.expected_terminal_value() - 5.3) < 0.05
