TREASURES = {
    "copper": {"value": 1, "cost": 0},
    "silver": {"value": 2, "cost": 3},
    "gold": {"value": 3, "cost": 6},
}

ACTIONS = {
    "festival": {"cost": 5, "actions": 2, "buy": 1, "value": 2},
    "laboratory": {"cost": 5, "actions": 1},
    "smithy": {"cost": 4, "draws": 3},
    "market": {"cost": 5, "draws": 1, "actions": 1, "buy": 1, "value": 1},
    "village": {"cost": 3, "draws": 1, "actions": 2},
}

VICTORIES = {
    "estate": {"cost": 2, "points": 1},
    "duchy": {"cost": 5, "points": 3},
    "province": {"cost": 8, "points": 6},
}


class Card:
    def buy_phase(self):
        return False

    def action_phase(self):
        return False

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Card) and self.name == other.name


class Treasure(Card):
    def __init__(self, name=None, cost=0, value=0):
        self.name = name
        self.cost = cost
        self.value = value

    def buy_phase(self):
        return True


class Action(Card):
    def __init__(self, name=None, cost=0, actions=0, buy=0, value=0, draws=0):
        self.name = name
        self.cost = cost
        self.actions = actions
        self.draws = draws
        self.buy = buy
        self.value = value

    def action_phase(self):
        return True


class Victory(Card):
    def __init__(self, name=None, cost=0, points=0):
        self.name = name
        self.cost = cost
        self.points = points
