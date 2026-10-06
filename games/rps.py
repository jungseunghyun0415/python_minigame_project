"""가위바위보 — 담당: 팀원 D

[규칙]
- 컴퓨터와 3판 2선승제로 대결한다.
- 입력: 1(가위) 2(바위) 3(보)

[구현 힌트]
- decide(player: str, computer: str) -> str  # "win" | "lose" | "draw"
"""

import random

GAME_NAME = "가위바위보"


def decide(player: str, computer: str) -> str:
    """플레이어와 컴퓨터의 결과를 판단한다."""
    if player == computer:
        return "draw"

    if (
        (player == "1" and computer == "3")
        or (player == "2" and computer == "1")
        or (player == "3" and computer == "2")
    ):
        return "win"

    return "lose"


def play() -> None:
    """3판 2선승을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    player_wins = 0
    computer_wins = 0

    choices = {
        "1": "가위",
        "2": "바위",
        "3": "보",
    }

    print(f"\n[{GAME_NAME}] 3판 2선승 게임을 시작합니다!")

    while player_wins < 2 and computer_wins < 2:
        player = input("선택하세요 (1:가위, 2:바위, 3:보): ")

        if player not in choices:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")
            continue

        computer = str(random.randint(1, 3))

        result = decide(player, computer)

        print(f"플레이어: {choices[player]}")
        print(f"컴퓨터: {choices[computer]}")

        if result == "win":
            player_wins += 1
            print("플레이어 승리!")
        elif result == "lose":
            computer_wins += 1
            print("컴퓨터 승리!")
        else:
            print("무승부!")

        print(f"현재 점수 → 플레이어 {player_wins} : {computer_wins} 컴퓨터\n")

    if player_wins == 2:
        print("🎉 최종 결과: 플레이어 승리!")
    else:
        print("😢 최종 결과: 컴퓨터 승리!")
