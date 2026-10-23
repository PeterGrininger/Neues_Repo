"""
USE: uv run python -m testing_course.connect_four
"""


# IMPORTS
from testing_course.connect_four.player import Player
from testing_course.connect_four.connect_four import InvalidMoveError


# ================
# SET SIZE OF GAME
# ================
ROWS = 6
COLS = 7
# ================


# ===================
# COLORS FOR PRINTING
# ===================
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"
# ===================


class ConnectFourGame:
    """
    Connect Four with ROWS and COLS, Players RED and YELLOW
    """

    def __init__(self, player_on_turn: Player) -> None:
        """
        Create empty game 
        player_on_turn makes the first move
        """

        self.field = [[] for _ in range(COLS)]
        self.on_turn = player_on_turn
        self.game_over = False
        self.game_winner = Player.NONE


    def get_player_at(self, row: int, col: int) -> Player:
        """
        Return the player at requested field, or Player.NONE if it is empty
        Raises IndexError if the field is outside the board
        """

        if not (0 <= row < ROWS and 0 <= col < COLS):
            raise IndexError(f"Field ({row}, {col}) is out of bounds")

        if row < len(self.field[col]):
            return self.field[col][row]

        return Player.NONE


    @property
    def player_on_turn(self) -> Player:
        """
        Return the player who makes the next move
        """

        return self.on_turn


    @property
    def is_game_over(self) -> bool:
        """
        Return True if someone has won or the board is full
        """

        return self.game_over


    @property
    def winner(self) -> Player:
        """
        Return the winner, Player.NONE if there is none (yet)
        """

        return self.game_winner


    def reset(self, player_on_turn: Player) -> None:
        """
        Clear the board and start a new game with player_on_turn
        """

        for cols in self.field:
            cols.clear()

        self.on_turn = player_on_turn
        self.game_over = False
        self.game_winner = Player.NONE


    def drop(self, col: int) -> None:
        """
        Drop a disc for the current player into the requested column (0-6)

        -> Drop Disc if valid
        -> Check if move won
        -> Change player
        
        Raises InvalidMoveError if game is over, the column does not exist or is full.
        """

        if self.game_over:
            raise InvalidMoveError("Game has already concluded")

        if not 0 <= col < COLS:
            raise InvalidMoveError("This is not a valid Move!")

        if len(self.field[col]) >= ROWS:
            raise InvalidMoveError("This column is already filled to the max")

        self.field[col].append(self.on_turn)
        row = len(self.field[col]) - 1

        # ONLY the new disc can make a winning move, old regions do not have to be checked
        # Check for ...
        #   Horiontal (0,1)
        #   Vertical  (1,0)
        #   Diagonal  (1,1)
        #   Diagonal  (1,-1)

        for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            count = 1

            # Check to the right
            r = row + dr
            c = col + dc
            while 0 <= r < ROWS and 0 <= c < COLS and self.get_player_at(r, c) == self.on_turn:
                count += 1
                r += dr
                c += dc

            # Check to the left
            r = row - dr
            c = col - dc
            while 0 <= r < ROWS and 0 <= c < COLS and self.get_player_at(r, c) == self.on_turn:
                count += 1
                r -= dr
                c -= dc

            # if counter reached 4 or higher this is a winning move
            if count >= 4:
                self.game_over = True
                self.game_winner = self.on_turn
                return

        # Check if the game is already full!
        full = True
        for column in self.field:
            if len(column) < ROWS:
                full = False

        if full:
            self.game_over = True
            return

        # Change the player on turn
        if self.on_turn == Player.RED:
            self.on_turn = Player.YELLOW
        else:
            self.on_turn = Player.RED

    def __str__(self) -> str:
        """
        Return the board as text (X = RED, O = YELLOW, . = empty)
        """

        text = ""

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS):
                player = self.get_player_at(row, col)
                if player == Player.RED:
                    text += f"{RED}X{RESET} "
                elif player == Player.YELLOW:
                    text += f"{YELLOW}O{RESET} "
                else:
                    text += ". "
            text += "\n"

        text += f"On turn: {self.on_turn.name}\n"
        return text
