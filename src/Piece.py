from pygame import sprite
#create each individual 's subclass so that they know what image they use
#also create outline of each class, whilst using the parent class effectively
#class Piece(pygame.sprite)

class Piece():
    
    def __init__(self, team): # team is a string, "white" or "black"
        self.team = team

    def teamCheck(self):
        return self.team

    def capture(self):
        #it leaves the board...
        pass

    def get_type(self):
        return self.type #CONTINUE FROM HERE: consider moving setImage here for more organized code, if
        #possible

    def get_image_path(self):
        return self.image_path