"""테스트 작성 예시 — 본인 게임의 테스트(tests/test_<게임>.py)도 이렇게 만드세요."""

import utils


def test_ask_int_accepts_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert utils.ask_int("? ", 1, 5) == 3


def test_ask_int_retries_on_invalid(monkeypatch):
    answers = iter(["abc", "9", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    assert utils.ask_int("? ", 1, 5) == 2


def test_ask_yes_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Y")
    assert utils.ask_yes_no("계속?") is True
