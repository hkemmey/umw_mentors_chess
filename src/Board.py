#Forswyth Edwards Notation (look up "string notation chess")
#do this if piece class stuff is already done with for now
#see if we can build a board class with said notation

class Board:

    board = [[], [], [], [], [], [], [], []] #fill later
    def __init__(self):
        self.defaultString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" #FEN starting position
        __init__(defaultString)

    def __init__(self, boardString):
        #use boardString here to piece together the board here
        for x in boardString:
            if (boardString[x:x+1] == " "):
                break

            currentChar = boardString[x:x+1]
            #no chance to test if this will work; my first time working with try statements
            try:
                currentChar = int(currentChar)
            except:
                pass
            else:
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
