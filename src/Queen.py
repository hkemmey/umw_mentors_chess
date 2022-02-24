from Piece import Piece
import pygame

class Queen(Piece):
    type = "Queen"
    def __init__(self, color):
        self.color = color

        if color == "black":
            self.image_path = "../images/bQueen.png"
        else:
            self.image_path = "../images/wQueen.png"
    
        # self.image_path = "../images/bQueen.png" if color == "black" else "../images/wQueen.png"

    def get_legal_moves(self, row, col):
        pass
