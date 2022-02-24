#Forswyth Edwards Notation (look up "string notation chess")
#do this if piece class stuff is already done with for now
#see if we can build a board class with said notation
from Piece import Piece
from Rook import Rook
from King import King
from Knight import Knight
from Pawn import Pawn 
from Bishop import Bishop
from Queen import Queen

class Board:
    defaultString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    #            try:
    #                int(s)
    #               #what happens if it is in integer
    #            except Exception as e:
    ###what happens if int(s) throws in error
    def __init__(self):
        row_strings = []

        row_str = ""
        for s in self.defaultString:
            try:
                x = int(s)
                row_str += ("*" * x)

            except Exception as e:
                if s == "/":
                    row_strings.append(row_str)
                    row_str = ""
                elif s == " ":
                    row_strings.append(row_str)
                    break
                else:
                    row_str += s

        boardArray = [[], [], [], [], [], [], [], []] #fill later
        cur_row = 0
        #print(row_strings)
        for row in boardArray:
            for c in row_strings[cur_row]:
                if c == 'r':
                    row.append(Rook("Black"))
                elif c == 'R':
                    row.append(Rook("White"))
                elif c == "p":
                    row.append(Pawn("Black"))
                elif c == "P":
                    row.append(Pawn("White"))
                elif c == "q":
                    row.append(Queen("Black"))
                elif c == "Q":
                    row.append(Queen("White"))
                elif c == "k":
                    row.append(King("Black"))
                elif c == "K":
                    row.append(King("White"))
                elif c == "b":
                    row.append(Bishop("Black"))
                elif c == "B":
                    row.append(Bishop("White"))
                elif c == "n":
                    row.append(Knight("Black"))
                elif c == "N":
                    row.append(Knight("White"))
                elif c == "*":
                    row.append(None)
            cur_row += 1
        self.boardArray = boardArray

    def resetBoard(self):
        pass

    def getPiece(self):
        #get a piece from a specified coordinate
        #also check if the specified spot is occupied by a piece
        pass

    def getBoard(self):
        return self.boardArray