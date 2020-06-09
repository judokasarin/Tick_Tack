def display_game(board):
    line = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    line = board
    print(f'{line[7]}|{line[8]}|{line[9]}')
    print('------')
    print(f'{line[4]}|{line[5]}|{line[6]}')
    print('------')
    print(f'{line[1]}|{line[2]}|{line[3]}')
    print(' ')
    print(' ')


def player_input():
    while True:
        marker= input('Player One Choose a marker X or O: ')
        if marker.upper() in ['X','O']:
            print(f'Player one has choose {marker.upper()}')
            return marker.upper()
            break
        else:
            print(f'{marker} is an invalid Input')
            continue



def space_check(board,position):
    if board[position] == ' ':
        return True       
    else:
        print('Choose a free postion on the board (1-9)')
        display_game(board)
        return False
           

def board_upd(board,marker):
    while True:
        position = input('Choose a loction you want to update from the numpad(1-9): ')
        if not position.isdigit():
            print('Invalid Postion, try again')
            continue
        else:
            position = int(position)
            if not space_check(board,position):
                continue
            else:
                board[position] = marker
                return board
                break


def win_check(board,mark):
       return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first(marker):
    from random import randint
    rand = randint(0,101)
    if(rand<51):
        print('Player One goes first')
        return marker
    else:
        print('Player two goes first')
        if(marker == 'X'):
            marker = 'O'
        else:
            marker = 'X'
        return marker    


def draw(board):
    return ( not (board[1] ==  ' ' or board[2]== ' ' or  board[3]== ' ' or  board[4]== ' ' or  board[5]== ' ' or  board[6]== ' ' or  board[7]== ' ' or  board[8]== ' ' or  board[9] == ' '))



board =['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
marker = 'X'
while True: 
    display_game(board)
    marker=player_input()
    if marker in ['X','O']:
        marker = choose_first(marker)
        break
    else:
        continue


while True:    
    board_upd(board,marker)
    display_game(board)
    if win_check(board,marker):
        print('You are the winner')
        break
    else:
        if draw(board):
            print('draw(board)')
            break
        else:
            if(marker == 'X'):
                marker = 'O'
            else:
                marker = 'X'
            continue

