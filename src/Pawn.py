import Piece
import pygame

class Pawn(Piece.Piece):
    piece_type = "Pawn"
    def __init__(self, color, row, col, size):
        self.color = color
        self.position = (row * size, col * size)
        if color == "Black":
            self.image_path = "../images/bPawn.png"
        else:
            self.image_path = "../images/wPawn.png"

        x_pixel, y_pixel = self.position
        self.coords = (row, col)
        super().__init__(color, size, x_pixel, y_pixel, self.image_path, row, col)


        # self.image_path = "../images/bPawn.png" if color == "black" else "../images/wPawn.png"

    def get_legal_moves(self):
        ##return list of tuples
        self.legal_moves = []
        row, col = self.coords
        if self.color == "White":
            self.legal_moves.append((row, col-1))
        else:
            self.legal_moves.append((row, col+1))
        return self.legal_moves
