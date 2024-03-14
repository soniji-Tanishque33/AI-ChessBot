from const import *
import os

class Piece:
    def __init__(self, name, color, value, loc = None, texture_rect = None):
        self.name = name
        self.color = color
        val_sign = -1 if color == "white" else 1
        self.value = value*val_sign
        self.loc = loc
        self.moves = []
        self.moved = False
        self._setloc()
        self.texture_rect = texture_rect

    def _setloc(self,size = 80):
        self.loc = os.path.join(f"assets/images/imgs-{size}px/{self.color}_{self.name}.png")

    def _add_moves(self, move):
        self.moves.append(move)

class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__("pawn", color,  1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__("knight", color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__("bishop", color, 3.001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__("rook", color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__("queen", color, 9.0)

class King(Piece):
    def __init__(self, color):
        super().__init__("king", color, 10000)