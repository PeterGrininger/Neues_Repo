from typing import Protocol

from testing_course.connect_four.player import Player


class InvalidMoveError(Exception):
    """Raised when a disc cannot be dropped (full column or finished game)."""


class ConnectFour(Protocol):
    def get_player_at(self, row: int, col: int) -> Player: ...

    @property
    def player_on_turn(self) -> Player: ...

    @property
    def is_game_over(self) -> bool: ...
    # Spielfeld voll kein Gewinner
    # Spieler ROT nach Zug/Auswertung
    # Spieler Gelb nach Zug/Auswertung

    @property
    def winner(self) -> Player: ...

    def reset(self, player_on_turn: Player) -> None: ...
    # Setze alle Felder auf Spieler None
    # for x for y feld == None

    def drop(self, col: int) -> None: ...
    
    # Logik Zug
    #   - player_on_turn()
    #   - Makiere Feld col/row

    # Logik Auswertung
    #   - "Nur" lokal um Stein
    #   - Gewinn/nicht Gewinn - winner 

    # Ändert Spieler am Zug - player on turn()
