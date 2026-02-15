import pytest
from src.board import Board
from src.player import Player
import src.pieces as pieces

@pytest.fixture
def game():
    """Initializes a standard game state."""
    b = Board()
    p1 = Player(b, 'w')
    p2 = Player(b, 'b')
    b.players = [p1, p2]
    b.update_available_moves()
    return b, p1, p2

def test_initial_pawn_moves(game):
    b, p1, p2 = game
    pawn = b.board[2][1]
    assert (3, 1) in pawn.available_moves
    assert (4, 1) in pawn.available_moves
    assert (5, 1) not in pawn.available_moves

def test_knight_moves(game):
    b, p1, p2 = game
    knight = b.board[1][2]
    # Knight at (1,2) can jump to (3,1) and (3,3)
    assert (3, 1) in knight.available_moves
    assert (3, 3) in knight.available_moves

def test_piece_capture(game):
    b, p1, p2 = game
    white_pawn = b.board[2][1]
    # Manually place a black pawn in capture range
    black_pawn = pieces.Pawn(b, 3, 2, 'b')
    p2.add_piece(black_pawn)
    b.update_pieces()
    b.update_available_moves()
    
    assert (3, 2) in white_pawn.available_moves

def test_check_detection(game):
    b, p1, p2 = game
    # Move white king to center
    king = p1.pieces[0]
    king.set_cell(4, 4)

    # Place black rook on same file
    rook = p2.pieces[2]
    rook.set_cell(4, 7)
    
    b.update_pieces()
    b.update_available_moves()
    
    assert b.check_check(True) is True

def test_sliding_piece_blocked_by_friend(game):
    b, p1, p2 = game
    rook = b.board[1][1]
    # Rook is blocked by pawn at (2,1) and knight at (1,2)
    assert len(rook.available_moves) == 0