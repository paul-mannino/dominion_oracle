# Summary

This is a library for computing statistics about the deck-building game Dominion. Right now, the simulator is extremely limited in what kinds of questions it can answer and what kinds of cards it can simluate, but hopefully this will grow with time.

## Example 1 - Choosing a card to buy

```
from dominion_oracle.simulation import BuyOneSimulation
from dominion_oracle.formatter import print_grid_table

deck = ["copper"] * 7 + ["estate"] * 3
candidates = ["copper", "silver", "duchy"]

simulation = BuyOneSimulation(deck, candidates)
y_vals, cell_vals = simulation.expected_terminal_values(n=10000)
print(simulation.description())
print_grid_table(y_vals=y_vals, cell_vals=cell_vals)
```

### Output

<pre>
Expected values for a base deck of copper * 7, estate * 3 and one card added
+--------+-------+
| (none) |  3.5  |
+--------+-------+
| copper | 3.629 |
+--------+-------+
| silver | 4.089 |
+--------+-------+
| duchy  | 3.192 |
+--------+-------+
</pre>


## Example 2 - Exploring 2-card interactions

```
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

```

### Output

<pre>
Expected values for a base deck of copper * 7, estate * 3, gold * 1
+-----------+----------+----------+----------+----------+----------+----------+
|           | 1 smithy | 2 smithy | 3 smithy | 4 smithy | 5 smithy | 6 smithy |
+-----------+----------+----------+----------+----------+----------+----------+
| 1 village |  5.223   |  5.625   |  5.633   |  5.463   |  5.218   |  4.965   |
+-----------+----------+----------+----------+----------+----------+----------+
| 2 village |  5.213   |  5.726   |  6.077   |  5.983   |  5.779   |  5.437   |
+-----------+----------+----------+----------+----------+----------+----------+
| 3 village |  5.215   |  5.891   |  6.399   |  6.564   |  6.439   |  6.168   |
+-----------+----------+----------+----------+----------+----------+----------+
| 4 village |  5.212   |  5.939   |  6.724   |  7.053   |  6.984   |   6.77   |
+-----------+----------+----------+----------+----------+----------+----------+
| 5 village |  5.218   |   6.06   |   6.96   |  7.416   |  7.521   |  7.397   |
+-----------+----------+----------+----------+----------+----------+----------+
</pre>
