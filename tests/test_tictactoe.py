from games.tictactoe import check_winner, is_full


def test_check_winner():
    board = [["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]]
    assert check_winner(board) == "X"


def test_is_full():
    board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    assert is_full(board) is True
