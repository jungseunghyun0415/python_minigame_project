"""숫자 야구 — 담당: 팀원 

[규칙]
- 컴퓨터가 서로 다른 숫자 3개를 정한다. (예: 3 7 1)
- 플레이어가 3자리를 추측하면 스트라이크(숫자·자리 모두 일치),
  볼(숫자만 일치)을 알려 준다. 최대 9번.

[구현 힌트]
- make_answer() -> str
- judge(answer: str, guess: str) -> tuple[int, int]   # (strike, ball)
"""

import random

GAME_NAME = "숫자 야구"

DIGITS = 3
MAX_TRIES = 9


def make_answer() -> str:
    """서로 다른 숫자 3개로 이루어진 정답 문자열을 만든다. 예: '371'"""
    return "".join(random.sample("0123456789", DIGITS))


def judge(answer: str, guess: str) -> tuple[int, int]:
    """(strike, ball)을 계산한다."""
    strike = sum(a == g for a, g in zip(answer, guess))
    ball = len(set(answer) & set(guess)) - strike
    return strike, ball


def is_valid_guess(guess: str) -> bool:
    """3자리 숫자이고, 서로 다른 숫자인지 확인한다."""
    return (
        len(guess) == DIGITS
        and guess.isdecimal()
        and len(set(guess)) == DIGITS
    )


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    answer = make_answer()

    print(f"\n=== {GAME_NAME} ===")
    print(f"컴퓨터가 서로 다른 숫자 {DIGITS}개를 정했어요. 맞혀 보세요!")
    print(f"기회는 최대 {MAX_TRIES}번이에요. (포기하려면 q 입력)\n")

    for turn in range(1, MAX_TRIES + 1):
        # 올바른 입력이 들어올 때까지 같은 턴에서 다시 묻는다.
        while True:
            guess = input(f"[{turn}/{MAX_TRIES}] 추측: ").strip()
            if guess.lower() == "q":
                print(f"포기했어요. 정답은 {answer}였습니다.")
                return
            if is_valid_guess(guess):
                break
            print(f"서로 다른 숫자 {DIGITS}개를 입력해 주세요. (예: 123)")

        strike, ball = judge(answer, guess)

        if strike == DIGITS:
            print(f"정답입니다! {turn}번 만에 맞혔어요. 🎉")
            return

        if strike == 0 and ball == 0:
            print("아웃!")
        else:
            print(f"{strike}S {ball}B")

    print(f"\n기회를 모두 사용했어요. 정답은 {answer}였습니다.")


if __name__ == "__main__":
    play()