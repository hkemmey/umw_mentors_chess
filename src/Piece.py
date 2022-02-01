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
    

def pawn(Piece):
    pass
