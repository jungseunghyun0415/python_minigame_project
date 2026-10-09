"""행맨 — 담당: 팀원 B

[규칙]
- 단어 목록에서 무작위로 하나를 고른다.
- 플레이어는 한 글자씩 추측하고, 틀리면 기회가 하나 줄어든다. (기회 6번)
- 맞힌 글자만 보여 준다.  예) a _ p l _

[구현 힌트] 테스트하기 쉽도록 순수 함수로 나눠 보세요.
- mask_word(word: str, guessed: set[str]) -> str
- is_solved(word: str, guessed: set[str]) -> bool
"""

import random

GAME_NAME = "행맨"
MAX_WRONG = 6
WORDS = [
    "apple", "banana", "python", "keyboard", "monitor",
    "elephant", "computer", "mountain", "library", "rainbow",
]


def mask_word(word: str, guessed: set[str]) -> str:
    """맞힌 글자만 드러내고 나머지는 _ 로 가린다. 예) 'apple', {'a','p'} -> 'a p p _ _'"""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def is_solved(word: str, guessed: set[str]) -> bool:
    """단어의 모든 글자를 맞혔는지 여부."""
    return all(ch in guessed for ch in word)


def wrong_guesses(word: str, guessed: set[str]) -> set[str]:
    """추측한 글자 중 단어에 없는 글자들."""
    return {ch for ch in guessed if ch not in word}


def _read_guess(guessed: set[str]) -> str:
    """유효한 한 글자 입력을 받을 때까지 반복한다."""
    while True:
        raw = input("글자를 입력하세요: ").strip().lower()
        if len(raw) != 1 or not raw.isalpha():
            print("알파벳 한 글자만 입력해 주세요.")
        elif raw in guessed:
            print("이미 추측한 글자입니다.")
        else:
            return raw


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    word = random.choice(WORDS)
    guessed: set[str] = set()

    print(f"\n=== {GAME_NAME} ===")
    while True:
        wrong = wrong_guesses(word, guessed)
        remaining = MAX_WRONG - len(wrong)

        print(f"\n단어: {mask_word(word, guessed)}")
        print(f"남은 기회: {remaining}  |  틀린 글자: {' '.join(sorted(wrong)) or '-'}")

        if is_solved(word, guessed):
            print(f"🎉 정답입니다! 단어는 '{word}' 였습니다.")
            return
        if remaining <= 0:
            print(f"💀 실패! 정답은 '{word}' 였습니다.")
            return

        guessed.add(_read_guess(guessed))


if __name__ == "__main__":
    play()