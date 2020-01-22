import curses

from .flameboard import FlameBoard

class CursesFlameBoard(FlameBoard):
    def __init__(self, screen):
        self.screen = screen
        self.chars = [' ', '.', '~', '*', 'x', 'X']
        self.chars_len = len(self.chars) - 1

        super().__init__(*screen.getmaxyx())

    def get_char(self, pos: int) -> str:
        """Maps value at pos to a character."""
        return self.chars[-1 if self.board[pos] > self.chars_len else self.board[pos]]

    def get_color(self, pos: int) -> int:
        """Distribute fire-y colours."""
        position_color = 1
        # Exponential distribution suits fire very well.
        #for n in range(2, 5):
        #    if board[pos] > n ** 2:
        #        position_color = n
        # Loop is too slow for many elements, so we check hardcoded values:
        if self.board[pos] > 16:
            position_color = 4
        elif self.board[pos] > 9:
            position_color = 3
        elif self.board[pos] > 4:
            position_color = 2

        return position_color

    def user_quit(self):
        """Checks if the user has pressed 'q'."""
        self.screen.refresh()
        self.screen.timeout(30)
        return self.screen.getch() == ord('q')

    def run(self):
        """Simulates fire in the terminal."""
        while True:
            for pos in self.iter_board():
                if pos < self.size - 1:
                    self.screen.addstr(
                            pos // self.width, # Y
                            pos % self.width,  # X
                            self.get_char(pos),
                            curses.color_pair(self.get_color(pos))
                        )
            if self.user_quit():
                break
