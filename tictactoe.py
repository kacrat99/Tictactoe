board = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ''
player2 = ''

def main_game(board):
    game_board(board)
    players = player_input()
    player1 = players[0]
    player2 = players[1]
    print("Player1 is: " + player1 + " player2 is: " + player2)
    put_in_move(p1_move(),board,player1)
    game_board(board)







def game_board(board):
    for x in range(1,len(board)):
        if x%3==0:
            print(board[x],end='')
            print()
        else:
            print(board[x]+'|',end='')


def put_in_move(x,board,player):
    board[x] = player
    if if_game_is_over(board):
        input('koniec gry, czy chcesz zagrac jeszcze raz?(yes/no)')



def if_game_is_over(board):
    return True



def koniec_gry(string):
    if string == 'yes':
        main_game()
    else:
        print("thanks for playing")
        exit()
def player_input():
    marker = ''
    while marker not in ['x','o']:
        marker = input('player1(x/o)')
        player1 = marker
        if player1 == 'x':
            player2 = 'o'
        else:
            player2 = 'x'

    return [player1,player2]

def p1_move():
    tmp = 0
    while tmp not in ['1','2','3','4','5','6','7','8','9']:
        tmp = input('player1 wybierz pole(1-9)')

    return int(tmp)
def p2_move():
    tmp = 0
    while tmp not in ['1','2','3','4','5','6','7','8','9']:
        tmp = input('player2 wybierz pole(1-9)')

    return int(tmp)

main_game(board)
