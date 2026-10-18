from games.rps import decide


def test_decide_win():
    assert decide("1", "3") == "win"
    assert decide("2", "1") == "win"
    assert decide("3", "2") == "win"


def test_decide_lose():
    assert decide("1", "2") == "lose"
    assert decide("2", "3") == "lose"
    assert decide("3", "1") == "lose"


def test_decide_draw():
    assert decide("1", "1") == "draw"
    assert decide("2", "2") == "draw"
    assert decide("3", "3") == "draw"
