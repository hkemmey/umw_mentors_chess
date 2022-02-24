import pygame
import Board
import Piece

game_Board = Board.Board() #Passing "" as an argument makes it default string

print(game_Board.boardArray)

class pieceSprite(pygame.sprite.Sprite):
    def __init__(self, size, x_pos, y_pos, team):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(team)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x_pos, y_pos]





WIDTH = HEIGHT = 512
NUM_SQUARES_PER_ROW = 8
SQ_SIZE = HEIGHT/NUM_SQUARES_PER_ROW
COLOR_LIGHT = "#FEE3BF"
COLOR_DARK = "#B28E5F"
BLACK_LINE = "#000000"

# initialize a pygame screen
# draw a grid
# ligther color and a darker color alternating squares
# Vertically, A-H, 1-8 Horizontally
# 
# Put the images onto the board
# return screen
def draw_board(screen):

    x = 0 #offset to the right
    y = 0 #offset downward

    prev_is_light = False

    while y <= HEIGHT - SQ_SIZE:
        if prev_is_light:
            #draw dark
            ##pygame.draw.rect(display, color, (x, y, SQ_SIZE, SQ_SIZE))
            ##pygame.draw.line(display, color, (x1, y1), (x2, y2))
            pygame.draw.rect(chess_board, COLOR_DARK, (x, y, SQ_SIZE, SQ_SIZE))

        else:
            #draw light
            pygame.draw.rect(chess_board, COLOR_LIGHT, (x, y, SQ_SIZE, SQ_SIZE))

        prev_is_light = True if prev_is_light == False else False

        if x < (WIDTH - SQ_SIZE):
            x += SQ_SIZE
        else:
            y += SQ_SIZE
            x = 0
            prev_is_light = True if prev_is_light == False else False

    x = 0
    y = 0

    while y < HEIGHT:
        if x < WIDTH:
            pygame.draw.line(screen, BLACK_LINE, (x, 0), (x, HEIGHT))
            x += SQ_SIZE
        else:
            pygame.draw.line(screen, BLACK_LINE, (0, y), (WIDTH, y))
            y += SQ_SIZE


def place_pieces(screen):
    #####Sprite (pygame documentation for sprites)#####
    
    pass

    
if __name__ == "__main__":

    pygame.init()
    piece = pieceSprite(SQ_SIZE, 0, 0, BLACK_LINE)


    piece_group = pygame.sprite.Group()
    piece_group.add(piece)
    chess_board = pygame.display.set_mode((WIDTH, HEIGHT))

    draw_board(chess_board)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        piece_group.draw(chess_board)
                


    