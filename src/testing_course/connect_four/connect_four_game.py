from testing_course.connect_four.player import Player
from testing_course.connect_four.connect_four import InvalidMoveError

ROWS = 6
COLS = 7

class ConnectFourGame:
    def __init__(self, player_on_turn: Player) -> None:
        self.field = [[] for _ in range(COLS)]
        self.on_turn = player_on_turn
        self.game_over = False
        self.game_winner = Player.NONE

    def get_player_at(self, row: int, col: int) -> Player:
        if not (0 <= row < ROWS and 0 <= col < COLS):
            raise IndexError(f"Field ({row}, {col}) is out of bounds")

        column = self.field[col]
        if row < len(column):
            return column[row]
        return Player.NONE

    @property
    def player_on_turn(self) -> Player:
        return self.on_turn

    @property
    def is_game_over(self) -> bool:
        return self.game_over

    @property
    def winner(self) -> Player:
        return self.game_winner

    def reset(self, player_on_turn: Player) -> None:
        for cols in self.field:
            cols.clear()

        self.on_turn = player_on_turn
        self.game_over = False
        self.game_winner = Player.NONE

    def drop(self, col: int) -> None:
        if self.game_over:
            raise InvalidMoveError("Game has already concluded")
        if not 0 <= col < COLS:
            raise InvalidMoveError("This is not a valid Move!")
        if len(self.field[col]) >= ROWS:
            raise InvalidMoveError("This column is already filled to the max")

        self.field[col].append(self.on_turn)
        row = len(self.field[col]) - 1

        if self._is_winning_move(row, col):
            self.game_over = True
            self.game_winner = self.on_turn
        elif all(len(c) == ROWS for c in self.field):
            self.game_over = True          
        else:
            self.on_turn = Player.YELLOW if self.on_turn == Player.RED else Player.RED

    def _is_winning_move(self, row: int, col: int) -> bool:
        player = self.get_player_at(row, col)
        for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
            count = 1
            count += self._count(row, col, dr, dc, player)
            count += self._count(row, col, -dr, -dc, player)
            if count >= 4:
                return True
        return False

    def _count(self, row: int, col: int, dr: int, dc: int, player: Player) -> int:
        count = 0
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and self.get_player_at(r, c) == player:
            count += 1
            r += dr
            c += dc
        return count
