import Board

class GameState:
    instance = None

    def get_instance():
        if instance == None:
            instance = GameStae()
        return instance

    def __init__(self):
        GameState.instance = get_instance()
        self.board = new Board()

    def get_board(self):
        return self.board
