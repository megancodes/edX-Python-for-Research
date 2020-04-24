import numpy as np

# Exercise 1
#For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3. Make a function create_board() that creates such
#a board, with values of integers 0.
def create_board(r,c):
    return np.zeros((r,c), dtype=int)

board = create_board(3,3)
print("#1")
print(board)


# Exercise 2
#Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, indicating the number of the player who places there.
#Create a function place(board, player, position) with player being the current player (an integer 1 or 2), and position a tuple of length
#2 specifying a desired location to place their marker. Only allow the current player to place a piece on the board (change the board position
#to their number) if that position is empty (zero).
#Use create_board() to store a board as board, and use place to have Player 1 place a piece on spot (0, 0).
def place(board, player, position):
    if board[position] == 0:
        board[position] = player

place(board, 1, (0,0))
print("#2")
print(board)


# Exercise 3
#Create a function possibilities(board) that returns a list of all positions (tuples) on the board that are not
#occupied (0). (Hint: numpy.where is a handy function that returns a list of indexes that meet a condition.)
def possibilities(board):
    available = np.where(board == 0)
    return list(zip(available[0], available[1]))

print("#3")
print(possibilities(board))


# Exercise 4
#Create a function random_place(board, player) that places a marker for the current player at random
#among all the available positions (those currently set to 0).
#board is already defined from previous exercises. Call random_place(board, player) to place a random
#marker for Player 2, and store this as board to update its value.
import random
random.seed(1)

def random_place(board, player):
    choices = possibilities(board)
    move = random.choice(choices)
    place(board, player, move)
    return board

print("#4")
print(random_place(board, 2))


# Exercise 5
#board is already defined from previous exercises. Use random_place(board, player) to place three pieces
#on board each for players 1 and 2.
board = create_board(3,3)

for round in range(3):
    for player in [1,2]:
        random_place(board, player)

print("#5")
print(board)


# Exercise 6
# Make a function row_win(board, player) that takes the player (integer) and determines if any row consists of only their marker.
# Have it return True if this condition is met and False otherwise.
# board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.
def row_win(board, player):
    if np.any(np.all(board==player, axis=1)): # this checks if any row contains all positions equal to player.
        return True
    else:
        return False

"""def row_win(board, player):
    for row in board:
        cells = []
        for cell in row:
            cells.append(cell)
        if int(cells[0]) == int(cells[1]) == int(cells[2]):
            return True
        else:
            return False """

print("#6")
print(row_win(board, 1))


# Exercise 7
# Make a function col_win(board, player) that takes the player (integer) and determines if any column consists of only their marker.
# Have it return True if this condition is met and False otherwise.
# board is already defined from previous exercises. Call col_win to check if Player 1 has a complete column.
def col_win(board, player):
    if np.any(np.all(board == player, axis=0)):
        return True
    else:
        return False

"""def col_win(board, player):
    for col in board.T:
        cells = []
        for cell in col:
            cells.append(cell)
        if int(cells[0]) == int(cells[1]) == int(cells[2]) == player:
            return True
        else:
            return False"""

print("#7")
print(col_win(board, 1))


# Exercise 8
# Finally, create a function diag_win(board, player) that tests if either diagonal of the board consists of only their marker. Have it return True if this condition is met, and False otherwise.
# board has been slightly modified from a previous exercise. Call diag_win to check if Player 2 has a complete diagonal.
def diag_win(board, player):
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False
"""board[1][1] = 2
print(board)
def diag_win(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False"""

print("#8")
print(diag_win(board, 2))


# Exercise 9
# Create a function evaluate(board) that uses row_win, col_win, and diag_win functions for both players. If one of them has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.
# board is already defined from previous exercises. Call evaluate to see if either player has won the game yet.
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) == True or col_win(board, player) == True or diag_win(board, player) == True:
            winner = player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

print("#9")
print(evaluate(board))


# Exercise 10
# create_board(), random_place(board, player), and evaluate(board) have been created in previous exercises. Create a function play_game() that:
# Creates a board.
# Alternates taking turns between two players (beginning with Player 1), placing a marker during each turn.
# Evaluates the board for a winner after each placement.
# Continues the game until one player wins (returning 1 or 2 to reflect the winning player), or the game is a draw (returning -1).
# Call play_game 1000 times, and store the results of the game in a list called results.
def play_game():
    board = create_board(3,3)
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner


print("#10")
random.seed(1)
print(play_game())

# Call play_game 1000 times, and store the results of the game in a list called results.
GAMES = 1000
results = [play_game() for i in range(GAMES)]
"""results =[]
for i in range(GAMES):
    results.append(play_game())"""
print(results)
print(results.count(1))

"""count = 0
for result in results:
    if result == 1:
        count += 1
print(count)"""


# Exercise 11
# In the previous exercise, we see that when guessing at random, it's better to go first, as expected. Let's see if Player 1 can improve their strategy.
# Create a function play_strategic_game(), where Player 1 always starts with the middle square, and otherwise both players place their markers randomly.
# Call play_strategic_game 1000 times.
def play_strategic_game():
    board = create_board(3, 3)
    board[1][1] = 1
    while True:
        for player in [2, 1]:
            random_place(board, player)
            result = evaluate(board)
            if result != 0:
                return result
                print(board)

print("#11")
random.seed(1)
print(play_strategic_game())

GAMES = 1000
new_results = [play_strategic_game() for i in range(GAMES)]
"""results =[]
for i in range(GAMES):
    results.append(play_strategic_game())"""

print(new_results)
print(new_results.count(1))