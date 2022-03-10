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

        boardArray = [[], [], [], [], [], [], [], []]
        cur_row = 0
        cur_col = 0
        #print(row_strings)
        from chess import SQ_SIZE #have to import here, otherwise circular import error occurs
        for row in boardArray:
            for c in row_strings[cur_col]:
                if c == 'r':
                    row.append(Rook("Black", cur_row, cur_col, SQ_SIZE))
                    print("bRook: " + str(cur_row) + " " + str(cur_col))
                elif c == 'R':
                    row.append(Rook("White", cur_row, cur_col, SQ_SIZE))
                    print("wRook: " + str(cur_row) + " " + str(cur_col))
                elif c == "p":
                    row.append(Pawn("Black", cur_row, cur_col, SQ_SIZE))
                elif c == "P":
                    row.append(Pawn("White", cur_row, cur_col, SQ_SIZE))
                elif c == "q":
                    row.append(Queen("Black", cur_row, cur_col, SQ_SIZE))
                elif c == "Q":
                    row.append(Queen("White", cur_row, cur_col, SQ_SIZE))
                elif c == "k":
                    row.append(King("Black", cur_row, cur_col, SQ_SIZE))
                elif c == "K":
                    row.append(King("White", cur_row, cur_col, SQ_SIZE))
                elif c == "b":
                    row.append(Bishop("Black", cur_row, cur_col, SQ_SIZE))
                elif c == "B":
                    row.append(Bishop("White", cur_row, cur_col, SQ_SIZE))
                elif c == "n":
                    row.append(Knight("Black", cur_row, cur_col, SQ_SIZE))
                elif c == "N":
                    row.append(Knight("White", cur_row, cur_col, SQ_SIZE))
                elif c == "*":
                    row.append(None)
                cur_row += 1
            cur_col += 1
            cur_row = 0
        self.boardArray = boardArray
        #print(boardArray)

    def resetBoard(self):
        pass

    def getPiece(self):
        #get a piece from a specified coordinate
        #also check if the specified spot is occupied by a piece
        pass

    def getBoard(self):
        return self.boardArray
