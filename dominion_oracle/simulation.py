import random
from collections import Counter
from dominion_oracle.cards import library


def shuffle_clone(deck):
    copy = deck[:]
    random.shuffle(copy)
    return copy


class Board:
    def __init__(self, card_list):
        self.deck = shuffle_clone(card_list)

    def draw(self, n=1):
        cards = []
        while self.deck and n > 0:
            cards.append(self.deck.pop())
            n -= 1
        return cards


HAND_SIZE = 5


def compressed_deck(deck):
    c = Counter(deck)
    return ", ".join([f"{card} * {count}" for card, count in c.items()])


class Simulation:
    def __init__(self, card_list):
        self.card_list = library.get_cards(card_list)

    def expected_terminal_value(self, n=10000):
        total = 0
        for _ in range(n):
            total += self.simulated_hand_value()
        return total / n

    def simulated_hand_value(self):
        """
        Basic strategy for basic set of cards. Play all cards that are at least neutral
        on actions, then play card draw, then return computed total value.
        """
        board = Board(self.card_list)
        hand = board.draw(HAND_SIZE)

        plus_actions = []
        terminal_actions = []
        rest = []

        def assign_card_to_pile(card):
            if card.action_phase():
                if card.actions >= 1:
                    plus_actions.append(card)
                else:
                    terminal_actions.append(card)
            else:
                rest.append(card)

        for card in hand:
            assign_card_to_pile(card)

        remaining_actions = 1
        running_value_total = 0
        while remaining_actions > 0 and (terminal_actions or plus_actions):
            if plus_actions:
                current_card = plus_actions.pop()
            else:
                current_card = terminal_actions.pop()

            for card in board.draw(n=current_card.draws):
                assign_card_to_pile(card)
            remaining_actions += current_card.actions - 1
            running_value_total += current_card.value
            remaining_actions - 1

        for card in filter(lambda c: c.buy_phase(), rest):
            running_value_total += card.value

        return running_value_total


class GridSimulation:
    def __init__(self, base_deck, card_x, card_y, x_min=1, x_max=1, y_min=1, y_max=1):
        self.base_deck = library.get_cards(base_deck)
        self.card_x = library.get_card(card_x)
        self.card_y = library.get_card(card_y)
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def expected_terminal_values(self, n=10000):
        x_vals = []
        y_vals = []
        z_vals = []
        for x in range(self.x_min, self.x_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                simulation = Simulation(self.base_deck + [self.card_x] * x + [self.card_y] * y)
                x_vals.append(x)
                y_vals.append(y)
                z_vals.append(simulation.expected_terminal_value(n=n))
        return x_vals, y_vals, z_vals

    def description(self):
        compressed = compressed_deck(self.base_deck)
        return f"Expected values for a base deck of {compressed}"


class BuyOneSimulation:
    def __init__(self, base_deck, buy_candidates):
        self.base_deck = library.get_cards(base_deck)
        self.buy_candidates = library.get_cards(buy_candidates)

    def expected_terminal_values(self, n=10000):
        x_vals = ["(none)"]
        y_vals = [Simulation(self.base_deck).expected_terminal_value(n=n)]
        for card in self.buy_candidates:
            simulation = Simulation(self.base_deck + [card])
            x_vals.append(card.name)
            y_vals.append(simulation.expected_terminal_value(n=n))
        return x_vals, y_vals

    def description(self):
        compressed = compressed_deck(self.base_deck)
        return f"Expected values for a base deck of {compressed} and one card added"
