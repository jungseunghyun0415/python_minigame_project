import pytest
import baseball  # baseball.py 파일을 불러옵니다.


# ----------------------------------------------------
# 1. 내부 로직 함수 테스트 (입출력 없음, 순수 연산 검증)
# ----------------------------------------------------

@pytest.mark.parametrize(
    "answer, guess, expected_strike, expected_ball",
    [
        ("371", "371", 3, 0),  # 3스트라이크 (정답)
        ("371", "317", 1, 2),  # 1스트라이크 2볼
        ("371", "713", 0, 3),  # 3볼
        ("371", "245", 0, 0),  # 아웃 (0S 0B)
    ],
)
def test_judge(answer, guess, expected_strike, expected_ball):
    """숫자 비교 로직이 정확히 동작하는지 검증"""
    strike, ball = baseball.judge(answer, guess)
    assert strike == expected_strike
    assert ball == expected_ball


@pytest.mark.parametrize(
    "guess, expected_valid",
    [
        ("123", True),
        ("112", False),  # 중복 숫자 탈락
        ("12", False),   # 자릿수 부족 탈락
        ("abc", False),  # 문자 입력 탈락
    ],
)
def test_is_valid_guess(guess, expected_valid):
    """사용자 입력 유효성 검증 함수 테스트"""
    assert baseball.is_valid_guess(guess) == expected_valid


def test_make_answer_format():
    """정답이 서로 다른 숫자 3개로 만들어지는지 검증"""
    for _ in range(100):
        answer = baseball.make_answer()
        assert len(answer) == 3
        assert answer.isdecimal()
        assert len(set(answer)) == 3


# ----------------------------------------------------
# 2. 게임 실행 시나리오 테스트 (입출력 시뮬레이션)
# ----------------------------------------------------

def test_play_win_scenario(monkeypatch, capsys):
    """플레이어가 한 번에 정답을 맞춰 승리하는 전체 시나리오"""
    # 컴퓨터 정답을 '371'로 강제 고정
    monkeypatch.setattr("random.sample", lambda pop, k: ["3", "7", "1"])

    # 플레이어가 첫 턴에 '371'을 입력했다고 시뮬레이션
    monkeypatch.setattr("builtins.input", lambda _: "371")

    baseball.play()

    captured = capsys.readouterr()
    assert "정답입니다! 1번 만에 맞혔어요." in captured.out


def test_play_give_up_scenario(monkeypatch, capsys):
    """플레이어가 'q'를 입력해 게임을 포기하는 시나리오"""
    monkeypatch.setattr("random.sample", lambda pop, k: ["3", "7", "1"])

    # 첫 번째는 틀린 값('123'), 두 번째는 포기('q')
    user_inputs = iter(["123", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    baseball.play()

    captured = capsys.readouterr()
    # 371과 123을 비교하면 0스트라이크 2볼
    assert "0S 2B" in captured.out
    assert "포기했어요. 정답은 371였습니다." in captured.out