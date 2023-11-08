from logic import check_winner
import logging
# add the log file record the games 
logging.basicConfig(
    filename='log/record.log',
    level=logging.INFO
)


def get_empty_board ():
    return [
    [None, None, None],
    [None, None, None],
    [None, None, None],
    ]
          
def print_board(board):
    for row in board:
        print(row)


def get_player_input():
    prompt= f"player {current_player} > \n "   #\n next line
    player_input = input(prompt) #this is a str
    
 
    row_col_list = player_input.split(',') # ["1","1"]
    row, col = [int(x)for x in row_col_list]
  
    return [row,col]

def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"

if __name__ == '__main__': #programe excute directly
    current_player = "X"
    board = get_empty_board()
    winner = None 
    
    while winner is None: 
        print_board(board)
        try:
           row, col = get_player_input()
        
        except ValueError:
            print("Invaild, try again")
            continue
        except IndexError:
            print("Invaild, try again")
            continue

        print(row)
        print(col)

        board[row][col] = current_player
        winner = check_winner(board)
        current_player = switch_player(current_player)

print(f"winner is {current_player}")
logging.info(f'Player {current_player} made a move')