import random

class FlameBoard:
    def __init__(self, height: int, width: int):
        self.height, self.width = height, width
        self.size = self.height * self.width

        self.board = [0] * (self.size + self.width + 1)

    def generate_row(self):
        """Sets values for row at the end of the board."""
        spread = 10 # TODO move to init, allow to be set.
        for _ in range(self.width // spread):
            self.board[
                int(
                    random.random() * self.width +  # Random position along...
                    self.width * (self.height - 1)  # ...the last row
                )
            ] = 100

    def decay_element(self, pos: int):
        """Sets the element at pos to be the mean of 4 nearby elements."""
        self.board[pos] = (
                self.board[pos] + self.board[pos+1] +
                self.board[pos+self.width] + self.board[pos+self.width+1]
            ) // 4

    def iter_board(self):
        self.generate_row()
        for pos in range(self.size):
            self.decay_element(pos)
            yield pos
