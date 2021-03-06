#REMEMBER TO CHANGE DIRECTORY TO SRC WHEN RUNNING!
import pygame
import Board
import Piece



WIDTH = HEIGHT = 512
NUM_SQUARES_PER_ROW = 8
SQ_SIZE = HEIGHT/NUM_SQUARES_PER_ROW
COLOR_LIGHT = "#FEE3BF"
COLOR_DARK = "#B28E5F"
BLACK_LINE = "#000000"



game_Board = Board.Board()

#print(game_Board.boardArray)
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

def pixel_xy_pos(x, y):
    x_pos = int(x / SQ_SIZE)
    y_pos = int(y / SQ_SIZE)
    return (x_pos, y_pos)

if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()

    piece_group = pygame.sprite.Group()
    for row in game_Board.boardArray:
        for piece in row:
            if piece == None:
                continue
            else:
                piece_group.add(piece)

    chess_board = pygame.display.set_mode((WIDTH, HEIGHT))

    draw_board(chess_board)
    print(chess_board)

    select_piece = None
    running = True

    col = None
    row = None
    player = "White"
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if select_piece == None:
                    col, row = pixel_xy_pos(x, y)
                    select_piece = game_Board.boardArray[row][col]
                    if select_piece != None and select_piece.color != player:
                        select_piece = None
                else:
                    col2, row2 = pixel_xy_pos(x, y)
                    #if the second click not a legal move do nothing
                    if (col2, row2) not in select_piece.get_legal_moves(game_Board.boardArray):
                        #print("breaking")
                        select_piece = None
                        break
                    #print("legal move")
                    if (col != col2 or row != row2): #player turn does not change
                        select_piece.set_pos(col2 * SQ_SIZE, row2 * SQ_SIZE)
                        if (select_piece != None):
                            piece_group.remove(game_Board.boardArray[row2][col2])
                        game_Board.boardArray[row2][col2] = game_Board.boardArray[row][col]
                        game_Board.boardArray[row][col] = None
                    select_piece.coords = (col2, row2)
                    select_piece = None
                    player = "Black" if player == "White" else "White" #only happens if turn is completed successfully, i.e not on illegal move attempts or move cancels
                #print(player + "'s Turn.")
    

        draw_board(chess_board)
        piece_group.draw(chess_board)
        pygame.display.flip()
        clock.tick(60)
