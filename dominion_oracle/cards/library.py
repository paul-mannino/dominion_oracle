from .card import Action, Treasure, Victory, Card, ACTIONS, TREASURES, VICTORIES


def _sanitize_name(name):
    return "_".join(word for word in name.lower().split(" "))


def _create_card(sanitized_name):
    if sanitized_name in ACTIONS:
        return Action(name=sanitized_name, **ACTIONS[sanitized_name])
    elif sanitized_name in TREASURES:
        return Treasure(name=sanitized_name, **TREASURES[sanitized_name])
    elif sanitized_name in VICTORIES:
        return Victory(name=sanitized_name, **VICTORIES[sanitized_name])

    raise ValueError(f"unknown card #{sanitized_name} for type")


registry = {}


def get_card(name):
    if isinstance(name, Card):
        return name

    sanitized_name = _sanitize_name(name)
    card = registry.get(sanitized_name, None)
    if card is None:
        card = _create_card(sanitized_name)
        registry[sanitized_name] = card
    return card


def get_cards(names):
    return [get_card(name) for name in names]
