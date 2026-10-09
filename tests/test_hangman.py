"""games/hangman.py 테스트 (pytest)

실행: 프로젝트 루트에서 `python -m pytest tests/test_hangman.py -v`
"""

import pytest

from games import hangman
from games.hangman import is_solved, mask_word, wrong_guesses


# ---------- mask_word ----------

def test_mask_word_nothing_guessed():
    assert mask_word("apple", set()) == "_ _ _ _ _"


def test_mask_word_partial():
    assert mask_word("apple", {"a", "e"}) == "a _ _ _ e"


def test_mask_word_reveals_all_repeated_letters():
    assert mask_word("apple", {"p"}) == "_ p p _ _"


def test_mask_word_all_guessed():
    assert mask_word("apple", set("apple")) == "a p p l e"


def test_mask_word_ignores_letters_not_in_word():
    assert mask_word("apple", {"z", "x"}) == "_ _ _ _ _"


def test_mask_word_empty_word():
    assert mask_word("", {"a"}) == ""


# ---------- is_solved ----------

def test_is_solved_false_when_nothing_guessed():
    assert is_solved("apple", set()) is False


def test_is_solved_false_when_partially_guessed():
    assert is_solved("apple", {"a", "p", "l"}) is False


def test_is_solved_true_when_all_letters_guessed():
    assert is_solved("apple", {"a", "p", "l", "e"}) is True


def test_is_solved_true_even_with_extra_wrong_guesses():
    assert is_solved("apple", {"a", "p", "l", "e", "z"}) is True


# ---------- wrong_guesses ----------

def test_wrong_guesses_only_returns_missing_letters():
    assert wrong_guesses("apple", {"a", "z", "q"}) == {"z", "q"}


def test_wrong_guesses_empty_when_all_correct():
    assert wrong_guesses("apple", {"a", "p"}) == set()


# ---------- play (입출력은 monkeypatch로 대체) ----------

@pytest.fixture
def run_game(monkeypatch, capsys):
    """정답 단어와 입력 목록을 정해 한 판을 실행하고 출력 문자열을 돌려준다."""

    def _run(word: str, inputs: list[str]) -> str:
        monkeypatch.setattr(hangman.random, "choice", lambda seq: word)
        answers = iter(inputs)
        monkeypatch.setattr("builtins.input", lambda *_: next(answers))
        hangman.play()
        return capsys.readouterr().out

    return _run


def test_play_win(run_game):
    out = run_game("cat", ["c", "a", "t"])
    assert "정답입니다" in out
    assert "실패" not in out


def test_play_lose_after_six_wrong_guesses(run_game):
    out = run_game("cat", ["x", "y", "z", "q", "w", "v"])
    assert "실패" in out
    assert "'cat'" in out
    assert "정답입니다" not in out


def test_play_wins_with_five_wrong_guesses(run_game):
    out = run_game("cat", ["x", "y", "z", "q", "w", "c", "a", "t"])
    assert "정답입니다" in out


def test_play_is_case_insensitive(run_game):
    out = run_game("cat", ["C", "A", "T"])
    assert "정답입니다" in out


@pytest.mark.parametrize("bad", ["", "ab", "1", "!", " "])
def test_play_invalid_input_does_not_cost_a_chance(run_game, bad):
    out = run_game("cat", [bad, "c", "a", "t"])
    assert "알파벳 한 글자만" in out
    assert "남은 기회: 6" in out
    assert "정답입니다" in out


def test_play_duplicate_guess_does_not_cost_a_chance(run_game):
    out = run_game("cat", ["x", "x", "c", "a", "t"])
    assert "이미 추측한 글자" in out
    assert "남은 기회: 5" in out
    assert "남은 기회: 4" not in out
    assert "정답입니다" in out