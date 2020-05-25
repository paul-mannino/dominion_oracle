from dominion_oracle.simulation import GridSimulation
from dominion_oracle.formatter import print_grid_table
from functools import partial

core_cards = ["copper"] * 7 + ["estate"] * 3 + ["gold"]
smithy = "smithy"
village = "village"


def label(entity, value):
    return f"{value} {entity}"


simulation = GridSimulation(core_cards, card_x=smithy, card_y=village, x_max=6, y_max=5)
x_vals, y_vals, cell_vals = simulation.expected_terminal_values(n=10000)
print(simulation.description())
print_grid_table(
    x_vals, y_vals, cell_vals, x_label=partial(label, smithy), y_label=partial(label, village)
)
