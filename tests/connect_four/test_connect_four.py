import pytest

from src.testing_course.connect_four import connect_four, connect_four_game, player
from testing_course.connect_four.connect_four_game import InvalidMoveError
from testing_course.connect_four.player import Player
from testing_course.connect_four.connect_four_game import ConnectFourGame
# Game ohne 4 in einer Reihe beide Spieler 

# Spieler x gewinnt,
#   - Horizontal
#   - Vertikal
#   - Diagonal

# ? 5 in einer Reihe/Spalte/Diagonale
# ? 2x,3x, ... 4 Gewinnt

# Spieler x wählte Spalte aus und legt Stein ->drop()
# ??? Wie testet man Reset == 0 Steiner ->reset()
# get_player_at() -INPUT Reihe/Spalte -OUTPUT Spieler Rot/Gelb/None

def test_initialization():
    #test player
    game = ConnectFourGame(Player.RED)
    assert game.player_on_turn == Player.RED
    #test game over
    assert not game.is_game_over
    #test game winner
    assert game.game_winner == Player.NONE

def test_get_player_at_out_of_bounds():
    #testing out of bounds
    game = ConnectFourGame(Player.RED)
    with pytest.raises(IndexError):
        game.get_player_at(-1,0)
    with pytest.raises(IndexError):
        game.get_player_at(6,0)
    with pytest.raises(IndexError):
        game.get_player_at(0,-1)
    with pytest.raises(IndexError):
        game.get_player_at(0,7)
        
def test_get_player_at_values():
    game = ConnectFourGame(Player.RED)
    #test before drop
    assert game.get_player_at(0,0) == Player.NONE
    game.drop(0)
    #test after drop
    assert game.get_player_at(0,0) == Player.RED

def test_drop_when_game_is_over():
    game = ConnectFourGame(Player.RED)
    #player red wins
    moves = [1, 1, 2, 2, 3, 3, 4]
    for col in moves:
        game.drop(col)
    #test is_game_over
    assert game.is_game_over
    #test move when game is over
    with pytest.raises(InvalidMoveError, match="Game has already concluded"):
        game.drop(5)
        
def test_invalid_column():
    #test invalid column move
    game = ConnectFourGame(Player.RED)
    for invalid_col in [-1,7,10]:
        with pytest.raises(InvalidMoveError, match="This is not a valid Move!"):
            game.drop(invalid_col)
            
def test_drop_full_column():
    game = ConnectFourGame(Player.RED)
    #fill col 1
    for _ in range(6):
        game.drop(1)
    # test move at filled col
    with pytest.raises(InvalidMoveError, match="This column is already filled to the max"):
        game.drop(1)
        
def test_horizontal_win():
    game = ConnectFourGame(Player.RED)
    #win on row 0 for player red
    for move in [1, 1, 2, 2, 3, 3, 4]:
        game.drop(move)
    assert game.is_game_over
    assert game.winner == Player.RED
    
def test_vertical_win():
    game = ConnectFourGame(Player.RED)
    #win on col 0 for player red
    for move in [1, 2, 1, 2, 1, 2, 1]:
        game.drop(move)
    assert game.is_game_over
    assert game.game_winner == Player.RED

def test_diagonal_win():
    #diagonal win for player red
    game = ConnectFourGame(Player.RED)
    for move in [1, 2, 3, 4, 2, 3, 4, 2, 3, 4, 4]:
        game.drop(move)
    assert game.is_game_over
    assert game.game_winner == Player.RED
    
def test_board_full():
    game = ConnectFourGame(Player.RED)
    #full board without a winner
    board_pattern = [
        0, 1, 0, 1, 0, 1,
        2, 3, 2, 3, 2, 3,
        1, 0, 1, 0, 1, 0,
        3, 2, 3, 2, 3, 2,
        4, 5, 4, 5, 4, 5,
        6, 4, 6, 4, 6, 4,
        5, 6, 5, 6, 5, 6
    ]
    for col in board_pattern:
        if not game.is_game_over:
            game.drop(col)
    assert game.is_game_over
    assert game.game_winner == Player.NONE
    
def test_reset():
    game = ConnectFourGame(Player.RED)
    game.drop(1)
    #Player red on 1,1
    assert game.get_player_at(0,1) == Player.RED
    
    game.reset(Player.YELLOW)
    #Player yellow on turn
    assert game.player_on_turn == Player.YELLOW
    #game is not over
    assert not game.is_game_over
    #no winner
    assert game.winner == Player.NONE
    #no player at 1,1
    assert game.get_player_at(0,1) == Player.NONE
    
def test_string_representation():
    #test str function
    game = ConnectFourGame(Player.RED)
    game.drop(1)
    game.drop(2)
    board_str = str(game)
    
    assert "X" in board_str
    assert "O" in board_str
    assert "On turn: RED" in board_str
    
