import pytest

from src.testing_course.connect_four import connect_four, connect_four_game, player

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
