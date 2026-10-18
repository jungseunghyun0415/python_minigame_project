"""공용 입력 도우미 — 담당: 팀원 A

모든 게임이 공통으로 사용합니다. 시그니처(함수 이름/인자)를 바꾸면
다른 팀원의 코드가 깨지므로, 변경 전에 팀에 먼저 알리세요.
"""


def ask_int(prompt: str, low: int, high: int) -> int:
    """low 이상 high 이하의 정수가 입력될 때까지 반복해서 묻는다."""
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-").isdigit() and low <= int(raw) <= high:
            return int(raw)
        print(f"{low}~{high} 사이의 숫자를 입력하세요.")


def ask_yes_no(prompt: str) -> bool:
    """y/n 입력을 받아 True/False 로 돌려준다."""
    while True:
        raw = input(prompt + " (y/n): ").strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("y 또는 n 으로 입력하세요.")


def format_title(title: str) -> str:
    """게임 제목을 보기 좋은 머리글 문자열로 만든다."""
    return f"=== {title} ==="
