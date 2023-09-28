# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.



import os

def display_board(board):
    os.system('cls' if os.name=='nt' else 'clear')
    print("  "+board[0]+" | "+board[1]+" | "+board[2])
    print("-----------")
    print("  "+board[3]+" | "+board[4]+" | "+board[5])
    print("-----------")
    print("  "+board[6]+" | "+board[7]+" | "+board[8])

def check_win(board, player):
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False

def tic_tac_toe():
    board = [" "]*9
    player = "X"
    cnt = 0
    while True:
        display_board(board)
        print("Игрок " + player + ", Ваш ход!")
        choice = input("Выберите клетку (1-9): ")
        try:
            choice = int(choice) - 1
            if board[choice] == " ":
                board[choice] = player
                cnt += 1
                if check_win(board, player):
                    display_board(board)
                    print("Игрок " + player + " победил!")
                    break
                elif cnt == 9:
                    display_board(board)
                    print("Ничья!")
                    break
                else:
                    player = "O" if player == "X" else "X"
            else:
                print("Клетка уже занята! Попробуйте снова.")
        except ValueError:
            print("Выберите число от 1 до 9!")

tic_tac_toe()