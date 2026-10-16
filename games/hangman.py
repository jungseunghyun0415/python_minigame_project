"""행맨 — 담당: 팀원 B

[규칙]
- 단어 목록에서 무작위로 하나를 고른다.
- 플레이어는 한 글자씩 추측하고, 틀리면 기회가 하나 줄어든다. (기회 6번)
- 맞힌 글자만 보여 준다.  예) a _ p l _

[구현 힌트] 테스트하기 쉽도록 순수 함수로 나눠 보세요.
- mask_word(word: str, guessed: set[str]) -> str
- is_solved(word: str, guessed: set[str]) -> bool
"""

GAME_NAME = "행맨"


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    # TODO: 구현하세요 (utils.ask_yes_no 등 공용 함수 활용 가능)
    print(f"[{GAME_NAME}] 아직 구현되지 않았습니다.")
