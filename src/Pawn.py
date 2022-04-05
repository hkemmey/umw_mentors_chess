import Piece
import pygame

class Pawn(Piece.Piece):
    piece_type = "Pawn"
    def __init__(self, color, x, y, size):
        self.color = color
        self.position = (x * size, y * size)
        if color == "Black":
            self.image_path = "../images/bPawn.png"
        else:
            self.image_path = "../images/wPawn.png"

        x1, y1 = self.position
        self.coords = (x, y)
        super().__init__(color, size, x1, y1, self.image_path)


        # self.image_path = "../images/bPawn.png" if color == "black" else "../images/wPawn.png"

    def get_legal_moves(self):
        ##return list of tuples
        legal_moves = []
        x, y = self.coords
        if self.color == "White":
            legal_moves.append((x, y-1))
        else:
            legal_moves.append((x, y+1))
        return legal_moves
