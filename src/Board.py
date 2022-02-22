#Forswyth Edwards Notation (look up "string notation chess")
#do this if piece class stuff is already done with for now
#see if we can build a board class with said notation
import Piece

class Board:
        

    def __init__(self, boardString):
        #use boardString here to piece together the board here
        self.defaultString = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" #FEN starting position

        if boardString == "":
            boardString = self.defaultString
        
        row = 0
        self.boardArray = [[], [], [], [], [], [], [], []] #fill later
        count = 0
        for x in boardString:
            if (x == " "):
                break

            
            #no chance to test if this will work; my first time working with try statements
            #also another thing im trying to figure out is whether or not its okay to really use this as a sort of/
            #if/else statement or not, mostly since the point of this is mostly just to prevent errors causing
            #the program to stop - Kevin
            
            try:
                blank_length = int(x)
            except:
                #match statement would be more functional, but the linter does not
                #recognize it as valid
                print("Except test:  " + x)
                if (x == "/"):
                    row += 1
                elif (x == "p"):
                   self.boardArray[row].append(Piece.pawn(False))
                elif (x == "P"):
                   self.boardArray[row].append(Piece.pawn(True))        
                elif (x == "r"): #lower case letter = black, black = False
                   self.boardArray[row].append(Piece.rook(False))
                elif (x == "R"):
                   self.boardArray[row].append(Piece.rook(True))
                elif (x == "n"):
                   self.boardArray[row].append(Piece.knight(False))
                elif (x == "N"):
                   self.boardArray[row].append(Piece.knight(True))
                elif (x == "b"):
                   self.boardArray[row].append(Piece.bishop(False))
                elif (x == "B"):
                   self.boardArray[row].append(Piece.bishop(True))
                elif ( x == "q"):
                   self.boardArray[row].append(Piece.queen(False))
                elif (x == "Q"):
                   self.boardArray[row].append(Piece.queen(True))    
                elif ( x == "k"):
                   self.boardArray[row].append(Piece.king(False))
                elif (x == "K"):
                   self.boardArray[row].append(Piece.king(True))        
            
            else:
                print("Else test  " + x)
                for n in range(blank_length):
                    #None is pythons version of null
                   self.boardArray[row].append(None)


    def resetBoard(self):
        pass
    def getPiece(self):
        #get a piece from a specified coordinate
        #also check if the specified spot is occupied by a piece
        pass

    def getBoard(self):
        return self.boardArray\





#This is here for testing purposes: get rid of it when filling the board works
gameBoard = Board("")
print(gameBoard.getBoard())