from dominion_oracle.cards import library


def test_create_treasure():
    card = library.get_card("Gold")
    assert card.name == "gold"
    assert card.value == 3
    assert card.cost == 6


def test_create_action():
    card = library.get_card("village")
    assert card.name == "village"
    assert card.value == 0
    assert card.cost == 3
    assert card.draws == 1
    assert card.actions == 2
    assert card.buy == 0
    assert card.value == 0
