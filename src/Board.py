#Forswyth Edwards Notation (look up "string notation chess")
#do this if piece class stuff is already done with for now
#see if we can build a board class with said notation
import Piece

class Board:

    board = [[], [], [], [], [], [], [], []] #fill later
    def __init__(self):
        self.defaultString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" #FEN starting position
        __init__(defaultString)

    def __init__(self, boardString):
        #use boardString here to piece together the board here
        row = 0
        for x in boardString:
            if (boardString[x:x+1] == " "):
                break

            currentChar = boardString[x:x+1]
            #no chance to test if this will work; my first time working with try statements
            #also another thing im trying to figure out is whether or not its okay to really use this as a sort of/
            #if/else statement or not, mostly since the point of this is mostly just to prevent errors causing
            #the program to stop - Kevin
            try:
                blank_length = int(currentChar)
            except:
                #match statement would be more functional, but the linter does not
                #recognize it as valid
                if (currentChar == "/"):
                    row += 1
                elif (currentChar == "r"): #lower case letter = black, black = False
                    board[row].append(Piece.rook(False))
                elif (currentChar == "R"):
                    board[row].append(Piece.rook(True))
                elif (currentChar == "n"):
                    board[row].append(Piece.knight(False))
                elif (currentChar == "N"):
                    board[row].append(Piece.knight(True))
                elif (currentChar == "b"):
                    board[row].append(Piece.bishop(False))
                elif (currentChar == "B"):
                    board[row].append(Piece.bishop(True))
                
            
            else:
                for i in blank_length:
                    #None is pythons version of null
                    board[row].append(None)


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
