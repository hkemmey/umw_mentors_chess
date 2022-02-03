#Forswyth Edwards Notation (look up "string notation chess")
#do this if piece class stuff is already done with for now
#see if we can build a board class with said notation

class Board:

    board = [[], [], [], [], [], [], [], []] #fill later
    def __init__(self):
        self.defaultString = ""
        __init__(defaultString)

    def __init__(self, boardString):
        #use boardString here to piece together the board here
        pass

    def resetBoard(self):
        pass
    def getPiece(self):
        #get a piece from a specified coordinate
        #also check if the specified spot is occupied by a piece
        pass

    def printBoard(self):
        #print all the pieces that are on the board as 2 letter symbols
        #example: bK = black King, wKn = white knight
        #empty spaces represented by "[_]"
        #maybe divide out all spaces with | and _
        pass
