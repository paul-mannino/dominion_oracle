from dominion_oracle.simulation import BuyOneSimulation
from dominion_oracle.formatter import print_grid_table

deck = ["copper"] * 7 + ["estate"] * 3
candidates = ["copper", "silver", "duchy"]

simulation = BuyOneSimulation(deck, candidates)
y_vals, cell_vals = simulation.expected_terminal_values(n=10000)
print(simulation.description())
print_grid_table(y_vals=y_vals, cell_vals=cell_vals)
