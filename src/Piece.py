#create each individual 's subclass so that they know what image they use
#also create outline of each class, whilst using the parent class effectively

from abc import ABC, abstractmethod

class Piece(ABC):
    dead = False
    team = False #VERY IMPORTANT: False = Black, True = White
    
    def __init__(self, team): #white is just a boolean that decides team
        self.t = team

    def updateTeam(self, team):
        self.t = team

    def teamCheck(self):
        return self.t

    def lifeUpdate(self, dead):
        self.life = dead

    def lifeStatus(self):
        return self.life
    
    def getType(self):
        return self.t #CONTINUE FROM HERE: consider moving setImage here for more organized code, if
        #possible
        

    class pawn():
        def __init__(self, team):
            super().__init__(team)
            self.t = "pawn"

        def setImage(self, team):
            if (team == False):
                image = "bPawn.png"
            else:
                image = "wPawn.png"
        
        def checkLegalMoves(self): #would this have to be defined in every class, or just the...
            #...parent class?
            pass
        #make a class that checks the position of the pawn, and sees if it has reached the other side

    class rook():
        def __init__(self, team):
            super().__init__(team)

        def setImage(self, team):
            if (team == False):
                image = "bRook.png"
            else:
                image = "wRook.png"
        
        def checkLegalMoves(self):
            pass

    class knight():
        def __init__(self, team):
            super().__init__(team)

        def setImage(self, team):
            if (team == False):
                image = "bKnight.png"
            else:
                image = "wKnight.png"
        
        def checkLegalMoves(self):
            pass    
        pass

    class bishop():
        def __init__(self, team):
            super().__init__(team)

        def setImage(self, team):
            if (team == False):
                image = "bBishop.png"
            else:
                image = "wBishop.png"
        
        def checkLegalMoves(self):
            pass    
        pass

    class queen():
        def __init__(self, team):
            super().__init__(team)

        def setImage(self, team):
            if (team == False):
                image = "bQueen.png"
            else:
                image = "wQueen.png"
        
        def checkLegalMoves(self):
            pass
        pass

    class king():
        def __init__(self, team):
            super().__init__(team)

        def setImage(self, team):
            if (team == False):
                image = "bKing.png"
            else:
                image = "wKing.png"
        
        def checkLegalMoves(self):
            pass    
        pass