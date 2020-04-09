from tictactoe import initial_state
from tictactoe import actions
from tictactoe import player
from tictactoe import result
from tictactoe import winner
from tictactoe import terminal
from tictactoe import utility
from tictactoe import minimax

X = "X"
O = "O"
EMPTY = None

myboard =   [[X, O, EMPTY],
            [O, EMPTY, O],
            [X, O, X]]
     
# z = [(i,j) for i in range(len(myboard)) for j in range(len(myboard[0])) if myboard[i][j] == EMPTY]
# print(z)
# print(actions(myboard))
# print(result(myboard,(1,1)))
# print(winner(myboard))
# print(terminal(myboard))
# print(utility(myboard))
print(player(myboard))
print(minimax(myboard))
