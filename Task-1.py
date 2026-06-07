# =========================================================
#               TIC-TAC-TOE AI USING PYTHON
#         Beginner-Friendly AI Internship Project
# =========================================================

# Import math module for infinity values
import math

# =========================================================
# Create an empty Tic-Tac-Toe board
# =========================================================
board = [" " for _ in range(9)]


# =========================================================
# Function to display the board
# =========================================================
def display_board():

    print("\n")

    print("     |     |     ")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("_____|_____|_____")

    print("     |     |     ")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("_____|_____|_____")

    print("     |     |     ")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")
    print("     |     |     ")

    print("\n")


# =========================================================
# Function to check if a player has won
# =========================================================
def check_winner(player):

    # All possible winning combinations
    winning_combinations = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    # Check each winning combination
    for combination in winning_combinations:

        if (
            board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player
        ):

            return True

    return False


# =========================================================
# Function to check if the game is a draw
# =========================================================
def check_draw():

    return " " not in board


# =========================================================
# Function for human player's move
# =========================================================
def player_move():

    while True:

        try:
            move = int(input("Enter your move (1-9): ")) - 1

            # Check if move is valid
            if move < 0 or move > 8:
                print("❌ Invalid position! Choose from 1 to 9.")

            # Check if position is already filled
            elif board[move] != " ":
                print("❌ Position already taken!")

            else:
                board[move] = "X"
                break

        except ValueError:
            print("❌ Please enter a valid number!")


# =========================================================
# Minimax Algorithm
# =========================================================
def minimax(is_maximizing):

    # If AI wins
    if check_winner("O"):
        return 1

    # If human wins
    if check_winner("X"):
        return -1

    # If draw
    if check_draw():
        return 0

    # =====================================================
    # AI Turn (Maximizing Player)
    # =====================================================
    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    # =====================================================
    # Human Turn (Minimizing Player)
    # =====================================================
    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


# =========================================================
# Function for AI move
# =========================================================
def ai_move():

    best_score = -math.inf
    best_move = 0

    # Check all possible moves
    for i in range(9):

        if board[i] == " ":

            # Try the move
            board[i] = "O"

            # Get score from minimax
            score = minimax(False)

            # Undo move
            board[i] = " "

            # Choose best move
            if score > best_score:

                best_score = score
                best_move = i

    # Place AI symbol
    board[best_move] = "O"

    print(f"\n🤖 AI chose position {best_move + 1}")


# =========================================================
# Main Game Function
# =========================================================
def play_game():

    global board

    # Reset board
    board = [" " for _ in range(9)]

    print("\n===================================")
    print("        TIC-TAC-TOE AI")
    print("===================================")

    print("\nYou are X")
    print("AI is O")

    print("\nBoard Positions:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")

    # Game loop
    while True:

        # Display board
        display_board()

        # Human move
        player_move()

        # Check if player wins
        if check_winner("X"):

            display_board()

            print("🎉 Congratulations! You win!")

            break

        # Check draw
        if check_draw():

            display_board()

            print("🤝 It's a draw!")

            break

        # AI move
        ai_move()

        # Check if AI wins
        if check_winner("O"):

            display_board()

            print("🤖 AI wins!")

            break

        # Check draw
        if check_draw():

            display_board()

            print("🤝 It's a draw!")

            break


# =========================================================
# Replay Option
# =========================================================
while True:

    play_game()

    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay != "yes":

        print("\n👋 Thanks for playing!")

        break


# =========================================================
#                    END OF PROGRAM
# =========================================================



"""
=========================================================
EXPLANATION OF MINIMAX ALGORITHM
=========================================================

The Minimax algorithm is an AI decision-making algorithm
commonly used in games like Tic-Tac-Toe.

HOW IT WORKS:
--------------
1. The AI checks all possible future moves.
2. It predicts the result of each move.
3. It gives scores:
      AI win   = +1
      Human win = -1
      Draw      = 0
4. The AI chooses the move with the best score.

WHY IT IS POWERFUL:
-------------------
The AI assumes the human will also play perfectly,
so it always chooses the safest and strongest move.

This makes the AI very difficult to beat.


=========================================================
HOW TO RUN THE PROGRAM
=========================================================

STEP 1:
Install Python on your computer.

STEP 2:
Save this file as:

    tic_tac_toe.py

STEP 3:
Open terminal or command prompt.

STEP 4:
Run the following command:

    python tic_tac_toe.py


=========================================================
SAMPLE OUTPUT
=========================================================

===================================
        TIC-TAC-TOE AI
===================================

You are X
AI is O

Board Positions:
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9


Enter your move (1-9): 5

🤖 AI chose position 1


     |     |
  O  |     |
_____|_____|_____
     |     |
     |  X  |
_____|_____|_____
     |     |
     |     |


=========================================================
"""