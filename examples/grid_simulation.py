from dominion_oracle.simulation import GridSimulation
from dominion_oracle.formatter import print_grid_table

core_cards = ["copper"] * 7 + ["estate"] * 3 + ["gold"]
smithy = "smithy"
village = "village"

simulation = GridSimulation(core_cards, card_x=smithy, card_y=village, x_max=6, y_max=5)
x_label = "{} " + smithy
y_label = "{} " + village
results = simulation.expected_terminal_values(n=10000)
print(simulation.description())
print_grid_table(results, x_label=x_label, y_label=y_label)
