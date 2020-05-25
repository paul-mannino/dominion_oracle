from beautifultable import BeautifulTable
from numbers import Number


def is_categorical(values):
    return any(not isinstance(value, Number) for value in values)


def default_label(value):
    return value


def _index_axis(values, start_val=0):
    indexed = {}
    current_val = start_val
    if is_categorical(values):
        sorted_values = values
    else:
        sorted_values = sorted(values)

    for value in sorted_values:
        if value not in indexed:
            indexed[value] = current_val
            current_val += 1

    return indexed


def _rows_for_3d(x_vals, y_vals, cell_vals, x_label, y_label):
    if len(x_vals) != len(y_vals) or len(x_vals) != len(cell_vals):
        raise ValueError("Lenghts of x vals, y vals, and cell values must match")

    indexed_x = _index_axis(x_vals)
    indexed_y = _index_axis(y_vals)
    n_cols = len(indexed_x)
    n_rows = len(indexed_y)

    if x_label is not None:
        n_rows += 1  # x labels need y space, vice versa
    if y_label is not None:
        n_cols += 1

    rows = [[""] * n_cols for _ in range(n_rows)]
    x_offset = 0 if y_label is None else 1
    if x_label:
        for x_value, x_index in indexed_x.items():
            rows[0][x_index + x_offset] = x_label(x_value)

    y_offset = 0 if x_label is None else 1
    if y_label:
        for y_value, y_index in indexed_y.items():
            rows[y_index + y_offset][0] = y_label(y_value)

    for idx in range(len(x_vals)):
        x_index = indexed_x[x_vals[idx]] + x_offset
        y_index = indexed_y[y_vals[idx]] + y_offset
        cell_value = cell_vals[idx]
        rows[y_index][x_index] = cell_value

    return rows


def print_grid_table(x_vals=None, y_vals=None, cell_vals=None, x_label=None, y_label=None):
    if y_vals is None or x_vals is None:
        # data is 2-dimensional rather than 3-dimensional
        if cell_vals is None:
            raise ValueError("cell_vals must be present")
        if x_vals is None:
            x_vals = [0] * len(y_vals)
            x_label = None
            y_label = y_label or default_label
        elif y_vals is None:
            y_vals = [0] * len(x_vals)
            y_label = None
            x_label = x_label or default_label
    else:
        x_label = x_label or default_label
        y_label = y_label or default_label

    rows = _rows_for_3d(x_vals, y_vals, cell_vals, x_label, y_label)
    table = BeautifulTable()
    for row in rows:
        table.append_row(row)

    print(table)
