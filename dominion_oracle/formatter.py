from beautifultable import BeautifulTable


def print_grid_table(triplets, x_label="{}", y_label="{}"):
    """
    Expected input format -- list of x value, y value, cell value
    Assumes non-sparse x & y values.
    """

    y_min = float("inf")
    y_max = float("-inf")
    x_min = float("inf")
    x_max = float("-inf")
    for x, y, _ in triplets:
        y_min = min(y, y_min)
        y_max = max(y, y_max)
        x_min = min(x, x_min)
        x_max = max(x, x_max)

    rows = [[""] * (x_max - x_min + 2) for _ in range(y_max - y_min + 2)]
    for x in range(x_min, x_max + 1):
        rows[0][x - x_min + 1] = x_label.format(x)

    for y in range(y_min, y_max + 1):
        rows[y - y_min + 1][0] = y_label.format(y)

    for x, y, value in triplets:
        rows[y - y_min + 1][x - x_min + 1] = value

    table = BeautifulTable()
    for row in rows:
        table.append_row(row)

    print(table)
