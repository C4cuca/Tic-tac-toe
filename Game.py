#Создаём поле
def print_board(board):
    print("\n  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()
    print()

#Начало игры
def play_game():
    board = [["-" for _ in range(3)] for _ in range(3)]
    players = ["1", "2"]
    current = 0

    print("Игра Крестики-нолики")
    print("Игрок 1 - X, Игрок 2 - O")

    for move in range(9): #Всего 9 ходов
        print_board(board)

        player_symbol = "X" if current == 0 else "O"
        print(f"Ход игрока {players[current]} ({player_symbol})")
        #Координаты
        try:
            row = int(input("Строка (0-2): "))
            col = int(input("Столбец (0-2): "))
        except:
            print("Ошибка! Введите числа 0-2")
            continue
        #Проверка координат
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Координаты вне поля!")
            continue

        if board[row][col] != "-":
            print("Клетка занята!")
            continue

        board[row][col] = player_symbol

        # Проверка победы
        if check_winner(board, player_symbol):
            print_board(board)
            print(f"Игрок {players[current]} победил!")
            return

        current = 1 - current

    print_board(board)
    print("Ничья!")


def check_winner(board, symbol):
    # Проверка строк
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True

    # Проверка столбцов
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == symbol:
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True

    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

#Старт игры
play_game()