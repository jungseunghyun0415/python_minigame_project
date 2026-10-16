GAME_NAME = "틱택토"

def check_winner(board: list[list[str]]) -> str | None:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board: list[list[str]]) -> bool:
    return all(cell != " " for row in board for cell in row)

def print_board(board: list[list[str]]) -> None:
    print()
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()

def play() -> None:
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print(f"\n=== {GAME_NAME} 게임을 시작합니다 ===")

    while True:
        print_board(board)
        try:
            user_input = input(f"[{current_player}] 위치 입력 (행 열, 예: 1 2) 또는 q(종료): ").strip()
            if user_input.lower() == "q": return
            r, c = map(int, user_input.split())
            r, c = r - 1, c - 1
            if not (0 <= r < 3 and 0 <= c < 3) or board[r][c] != " ":
                print("잘못된 입력이거나 이미 놓인 자리입니다.")
                continue
        except ValueError:
            print("숫자 2개를 띄어쓰기로 입력하세요.")
            continue

        board[r][c] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"축하합니다! [{winner}] 승리!")
            break
        if is_full(board):
            print_board(board)
            print("무승부입니다!")
            break
        current_player = "O" if current_player == "X" else "X"
