from pygame import sprite
import pygame
#create each individual 's subclass so that they know what image they use
#also create outline of each class, whilst using the parent class effectively
#class Piece(pygame.sprite)

class Piece(sprite.Sprite):

    def __init__(self, team, size, x_pos, y_pos, image_path, row, col): # team is a string, "white" or "black"
        super().__init__()
        size = [size, size]
        self.coords = (row, col)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x_pos, y_pos]
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

    def set_pos(self, x, y):
        self.rect.topleft = [x, y]
