from dominion_oracle.cards import create_card


def test_create_treasure():
    card = create_card("Gold")
    assert card.name == "gold"
    assert card.value == 3
    assert card.cost == 6


def test_create_action():
    card = create_card("village")
    assert card.name == "village"
    assert card.value == 0
    assert card.cost == 3
    assert card.draws == 1
    assert card.actions == 2
    assert card.buy == 0
    assert card.value == 0
