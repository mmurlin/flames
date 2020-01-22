import curses

from boards.cursesboard import CursesFlameBoard

def main():
    # Setup curses.
    screen = curses.initscr()

    # Make curse-or invisible.
    curses.curs_set(0)

    # Makes screen pretty.
    # TODO This is just what looks best on my setup, allow user to choose.
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)
    curses.init_pair(3, curses.COLOR_BLUE, -1)
    curses.init_pair(4, curses.COLOR_WHITE, -1)

    # Makes screen break less often.
    screen.refresh()

    fire = CursesFlameBoard(screen)
    fire.run() # Runs until the user presses 'q'.

    curses.endwin()

if __name__ == '__main__':
    main()
