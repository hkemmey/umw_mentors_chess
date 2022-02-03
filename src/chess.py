import pygame as pg

WIDTH = HEIGHT = 512
SPOTS = 8
SQ_SIZE = HEIGHT/SPOTS


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    while 1:
        screen.fill((255, 255, 255))
        pg.display.flip()

if __name__ == "__main__":
    main()