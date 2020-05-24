import random


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


class Simulation:
    def __init__(self, card_list):
        self.card_list = card_list

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
            remaining_actions += current_card.actions
            running_value_total += current_card.value

        for card in filter(lambda c: c.buy_phase(), rest):
            running_value_total += card.value

        return running_value_total
