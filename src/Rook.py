import Piece
import pygame

class Rook(Piece.Piece):
    piece_type = "Rook"
    def __init__(self, color, row, col, size):
        self.color = color
        self.position = (row * size, col * size)
        if color == "Black":
            self.image_path = "../images/bRook.png"
            #print("bRook coords: " + str(x*size) + ", " + str(y*size))
        else:
            self.image_path = "../images/wRook.png"
            #print("wRook coords: " + str(x*size) + ", " + str(y*size))

        x_pixel, y_pixel = self.position
        super().__init__(color, size, x_pixel, y_pixel, self.image_path, row, col)
    
        # self.image_path = "../images/bRook.png" if color == "black" else "../images/wRook.png"

    def get_legal_moves(self, row, col):
        pass

