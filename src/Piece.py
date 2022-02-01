from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, team):
        #defines all the traits that all pieces have in common
        #coordinates and team are shared traits
    def getCoordinate(self):
        #retrieves the coordinate of the piece as 2 integers, xCoord and YCoorc
    def getTeam(self):
        #retrieves the team of the piece as a boolean

        