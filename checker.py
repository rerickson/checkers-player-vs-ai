class Checker:
    def __init__(self, row, col, player_number: int):
        self.row: int = row
        self.col: int = col
        self.king = False
        self.x = 0
        self.y = 0
        self.radius_base = 50
        self.radius_top = 40
        self.player_number: int = player_number
        self.calc_center()

    # todo move this to UI
    def calc_center(self):
        self.x = 100 * self.col + 50
        self.y = 100 * self.row + 50

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_center()

    def make_king(self):
        self.king = True

    def get_player(self):
        return self.player_number